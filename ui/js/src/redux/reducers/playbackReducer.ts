import { createSlice } from '@reduxjs/toolkit';
import { ThunkAction } from 'redux-thunk';
import { PlaybackEntry, PlaybackState, ReduxState } from '../types';
import { selectEpisodes, selectPlaybackLog } from '../selectors';

type ThunkResult<R> = ThunkAction<R, ReduxState, undefined, any>;

const initialState: PlaybackState = {
  episode: null,
  logIdx: null,
  watchedEpisodes: [],
};

export function stepPlayback(): ThunkResult<void> {
  return (dispatch, getState) => {
    const state = getState();
    const playbackLog = selectPlaybackLog(state);
    const episodeCount = selectEpisodes(state).length;
    const { nextIdx, nextEpisode } = takeStep(
      state.playback,
      episodeCount,
      playbackLog.length,
    );

    dispatch({
      type: playbackSlice.actions.stepPlayback.type,
      payload: { nextIdx, nextEpisode },
    });

    const wait = determineWaitPeriod(
      playbackLog,
      state.playback.episode !== nextEpisode,
      nextIdx,
    );
    setTimeout(() => dispatch(stepPlayback()), wait);
  };
}

const playbackSlice = createSlice({
  name: 'playback',
  initialState,
  reducers: {
    stepPlayback(state, action) {
      const { nextIdx, nextEpisode } = action.payload;
      state.logIdx = nextIdx;
      state.episode = nextEpisode;
      if (nextEpisode != null) {
        state.watchedEpisodes.push(nextEpisode);
      }
    },
  },
});

function takeStep(
  state: PlaybackState,
  episodeCount: number,
  logCount: number,
) {
  if (episodeCount === 0) {
    return { nextIdx: null, nextEpisode: null };
  }
  if (state.episode !== null) {
    let nextIdx = (state.logIdx as number) + 1;
    if (nextIdx < logCount) {
      return { nextIdx, nextEpisode: state.episode };
    }
  }

  let nextEpisode = nextAvailableEpisode(
    episodeCount,
    new Set(state.watchedEpisodes),
  );
  if (nextEpisode !== null) {
    return { nextIdx: 0, nextEpisode };
  }

  return { nextIdx: null, nextEpisode: null };
}

function nextAvailableEpisode(
  episodeCount: number,
  watchedEpisodes: Set<number>,
) {
  for (let idx = episodeCount - 1; idx >= 0; idx--) {
    if (!watchedEpisodes.has(idx)) {
      return idx;
    }
  }
  return null;
}

function determineWaitPeriod(
  playbackLog: PlaybackEntry[],
  newEpisode: boolean,
  nextIdx: number | null,
) {
  if (newEpisode || nextIdx === null || nextIdx >= playbackLog.length) {
    return 1000;
  }

  const entry = playbackLog[nextIdx];
  if (entry.moveInfo.illegalMoves.length > 0) {
    return 500;
  }
  return 1000;
}

export default playbackSlice.reducer;
