import { createSlice } from '@reduxjs/toolkit';
import { ThunkAction } from 'redux-thunk';
import { PlaybackEntry, PlaybackState, ReduxState } from '../types';
import { selectEpisodes, selectPlaybackLog } from '../selectors';

type ThunkResult<R> = ThunkAction<R, ReduxState, undefined, any>;

const initialState: PlaybackState = {
  episode: null,
  logIdx: null,
  paused: false,
  watchedEpisodes: [],
};

export function stepPlayback(): ThunkResult<void> {
  return (dispatch, getState) => {
    const state = getState();
    if (state.playback.paused) {
      return;
    }

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

export function togglePlayback(episodeIter: number): ThunkResult<void> {
  return (dispatch, getState) => {
    const state = getState();

    const wasPaused = state.playback.paused;
    let shouldPause = !wasPaused;
    let episodeToPlay = undefined;
    if (episodeIter !== state.playback.episode) {
      episodeToPlay = episodeIter;
      shouldPause = false;
    }

    dispatch({
      type: playbackSlice.actions.togglePlayback.type,
      payload: { episodeToPlay, shouldPause },
    });

    if (wasPaused && !shouldPause) {
      setTimeout(() => dispatch(stepPlayback()), 0);
    }
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
    togglePlayback(state, action) {
      const { episodeToPlay, shouldPause } = action.payload;
      state.paused = shouldPause;
      if (episodeToPlay !== undefined) {
        state.episode = episodeToPlay;
        state.logIdx = 0;
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
