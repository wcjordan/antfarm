import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import { Episode, Step, TrainingRun } from './types';

type TrainingState = {
  episodes: Episode[];
  episodesLoading: boolean;
  steps: Step[];
  trainingRun: TrainingRun | null;
};

const initialState: TrainingState = {
  episodes: [],
  episodesLoading: false,
  steps: [],
  trainingRun: null,
};

export const fetchEpisodes = createAsyncThunk<
  Episode[],
  undefined,
  {
    state: TrainingState;
  }
>(
  'training/fetchEpisodes',
  async () => {
    const response = await fetch(
      'api/training/episodes/',
      getRequestOpts('GET'),
    );
    return await response.json();
  },
  {
    condition: (_unused, { getState }) => {
      return !getState().episodesLoading;
    },
  },
);

export const startTraining = createAsyncThunk(
  'training/startTraining',
  async () => {
    const options = getRequestOpts('POST');
    options['body'] = JSON.stringify({
      name: 'test run ' + new Date().toLocaleString(),
    });

    const response = await fetch('api/training/training_runs/', options);
    return await response.json();
  },
);

const trainingSlice = createSlice({
  name: 'training',
  initialState,
  reducers: {},
  extraReducers: {
    [fetchEpisodes.pending.type]: state => {
      state.episodesLoading = true;
    },
    [fetchEpisodes.fulfilled.type]: (state, action) => {
      state.episodesLoading = false;
      state.episodes = action.payload;
    },
    [fetchEpisodes.rejected.type]: state => {
      state.episodesLoading = false;
    },
    [startTraining.fulfilled.type]: (state, action) => {
      state.trainingRun = action.payload;
    },
  },
});

function getRequestOpts(method: string): RequestInit {
  return {
    credentials: 'same-origin',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    },
    method: method,
  };
}

export default trainingSlice.reducer;
