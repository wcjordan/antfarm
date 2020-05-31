import _ from 'lodash';
import { createSlice } from '@reduxjs/toolkit';
import { ThunkAction } from 'redux-thunk';
import {
  Episode,
  PlaybackEntry,
  PlaybackState,
  ReduxState,
  SortMode,
} from '../types';
import { selectPlaybackLog, selectSortedEpisodes } from '../selectors';

type ThunkResult<R> = ThunkAction<R, ReduxState, undefined, any>;

const initialState: PlaybackState = {
  episodeId: null,
  logIdx: null,
  paused: false,
  sortMode: SortMode.TotalReward,
  watchedEpisodes: [],
};

export function stepPlayback(): ThunkResult<void> {
  return (dispatch, getState) => {
    const state = getState();
    if (state.playback.paused) {
      return;
    }

    const playbackLog = selectPlaybackLog(state);
    const sortedEpisodes = selectSortedEpisodes(state);
    const { nextIdx, nextEpisodeId } = takeStep(
      sortedEpisodes,
      state.playback,
      playbackLog.length,
    );

    dispatch({
      type: playbackSlice.actions.stepPlayback.type,
      payload: { nextIdx, nextEpisodeId },
    });

    const wait = determineWaitPeriod(
      playbackLog,
      state.playback.episodeId !== nextEpisodeId,
      nextIdx,
    );
    setTimeout(() => dispatch(stepPlayback()), wait);
  };
}

export function togglePlayback(episodeId: number): ThunkResult<void> {
  return (dispatch, getState) => {
    const state = getState();

    const wasPaused = state.playback.paused;
    let shouldPause = !wasPaused;
    let episodeToPlay = undefined;
    if (episodeId !== state.playback.episodeId) {
      episodeToPlay = episodeId;
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
      const { nextIdx, nextEpisodeId } = action.payload;
      state.logIdx = nextIdx;
      state.episodeId = nextEpisodeId;
      if (nextEpisodeId != null) {
        state.watchedEpisodes.push(nextEpisodeId);
      }
    },
    togglePlayback(state, action) {
      const { episodeToPlay, shouldPause } = action.payload;
      state.paused = shouldPause;
      if (episodeToPlay !== undefined) {
        state.episodeId = episodeToPlay;
        state.logIdx = 0;
      }
    },
    toggleSortMode(state) {
      if (state.sortMode === SortMode.Iteration) {
        state.sortMode = SortMode.TotalReward;
      } else {
        state.sortMode = SortMode.Iteration;
      }
    },
  },
});

function takeStep(
  sortedEpisodes: Array<Episode>,
  state: PlaybackState,
  logCount: number,
) {
  if (sortedEpisodes.length === 0) {
    return { nextIdx: null, nextEpisodeId: null };
  }
  if (state.episodeId !== null) {
    let nextIdx = (state.logIdx as number) + 1;
    if (nextIdx < logCount) {
      return { nextIdx, nextEpisodeId: state.episodeId };
    }
  }

  let nextEpisodeId = nextAvailableEpisode(
    sortedEpisodes,
    new Set(state.watchedEpisodes),
  );
  if (nextEpisodeId !== null) {
    return { nextIdx: 0, nextEpisodeId };
  }

  return { nextIdx: null, nextEpisodeId: null };
}

function nextAvailableEpisode(
  sortedEpisodes: Array<Episode>,
  watchedEpisodes: Set<number>,
) {
  const match = _.find(sortedEpisodes, episode => {
    if (!watchedEpisodes.has(episode.id)) {
      return true;
    }
    return false;
  });

  if (match) {
    return match.id;
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
  } else if (entry.isDone) {
    return 2500;
  }
  return 1000;
}

export default playbackSlice.reducer;
