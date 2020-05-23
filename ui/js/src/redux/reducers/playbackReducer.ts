import { createSlice } from '@reduxjs/toolkit';
import { ThunkAction } from 'redux-thunk';
import { PlaybackState, ReduxState } from '../types';
import { selectEpisodes, selectSteps } from '../selectors';

type ThunkResult<R> = ThunkAction<R, ReduxState, undefined, any>;

const initialState: PlaybackState = {
  episode: null,
  step: null,
  playerMoveStep: false,
};

export function stepPlayback(): ThunkResult<void> {
  return (dispatch, getState) => {
    const state = getState();
    const stepCount = selectSteps(state).length;
    const episodeCount = selectEpisodes(state).length;
    dispatch({
      type: playbackSlice.actions.stepPlayback.type,
      payload: { stepCount, episodeCount },
    });
  };
}

const playbackSlice = createSlice({
  name: 'playback',
  initialState,
  reducers: {
    stepPlayback(state, action) {
      if (state.playerMoveStep) {
        state.playerMoveStep = false;
        return;
      }
      state.playerMoveStep = true;

      const { stepCount, episodeCount } = action.payload;
      const { nextStep, nextEpisode } = takeStep(
        state,
        stepCount,
        episodeCount,
      );
      state.step = nextStep;
      state.episode = nextEpisode;
    },
  },
});

function takeStep(
  state: PlaybackState,
  stepCount: number,
  episodeCount: number,
) {
  if (state.episode === null) {
    return { nextStep: 0, nextEpisode: 0 };
  }

  let nextStep = (state.step as number) + 1;
  if (nextStep < stepCount) {
    return { nextStep, nextEpisode: state.episode };
  }

  let nextEpisode = (state.episode as number) + 1;
  nextStep = 0;
  if (nextEpisode < episodeCount) {
    return { nextStep, nextEpisode };
  }

  return { nextStep: null, nextEpisode: null };
}

export default playbackSlice.reducer;
