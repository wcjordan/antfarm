import { createSlice } from '@reduxjs/toolkit';
import { ThunkAction } from 'redux-thunk';
import { PlaybackState, ReduxState } from '../types';
import { selectEpisodes, selectPlaybackLog } from '../selectors';

type ThunkResult<R> = ThunkAction<R, ReduxState, undefined, any>;

const initialState: PlaybackState = {
  episode: null,
  logIdx: null,
};

export function stepPlayback(): ThunkResult<void> {
  return (dispatch, getState) => {
    const state = getState();
    const logCount = selectPlaybackLog(state).length;
    const episodeCount = selectEpisodes(state).length;
    dispatch({
      type: playbackSlice.actions.stepPlayback.type,
      payload: { episodeCount, logCount },
    });
  };
}

const playbackSlice = createSlice({
  name: 'playback',
  initialState,
  reducers: {
    stepPlayback(state, action) {
      const { episodeCount, logCount } = action.payload;

      const { nextIdx, nextEpisode } = takeStep(state, episodeCount, logCount);
      state.logIdx = nextIdx;
      state.episode = nextEpisode;
    },
  },
});

function takeStep(
  state: PlaybackState,
  episodeCount: number,
  logCount: number,
) {
  if (state.episode === null) {
    return { nextIdx: 0, nextEpisode: 0 };
  }

  let nextIdx = (state.logIdx as number) + 1;
  if (nextIdx < logCount) {
    return { nextIdx, nextEpisode: state.episode };
  }

  let nextEpisode = (state.episode as number) + 1;
  nextIdx = 0;
  if (nextEpisode < episodeCount) {
    return { nextIdx, nextEpisode };
  }

  return { nextIdx: null, nextEpisode: null };
}

export default playbackSlice.reducer;
