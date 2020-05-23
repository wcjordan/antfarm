import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import { TrainingState } from '../types';
import getRequestOpts from '../getRequestOptions';

const initialState: TrainingState = {
  trainingRun: null,
};

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
    [startTraining.fulfilled.type]: (state, action) => {
      state.trainingRun = action.payload;
    },
  },
});

export default trainingSlice.reducer;
