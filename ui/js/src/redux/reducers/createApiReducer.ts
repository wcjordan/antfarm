import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import { ApiState, ReduxState } from '../types';
import getRequestOpts from '../getRequestOptions';

interface SliceGetter<T> {
  (state: ReduxState): ApiState<T>;
}

export default function createApiReducer<T>(
  apiName: string,
  apiUri: string,
  getSlice: SliceGetter<T>,
) {
  const initialState: ApiState<T> = {
    entries: [],
    loading: false,
  };

  const fetchThunk = createAsyncThunk<
    T[],
    void,
    {
      state: ReduxState;
    }
  >(
    `${apiName}/fetch`,
    async () => {
      const response = await fetch(apiUri, getRequestOpts('GET'));
      return await response.json();
    },
    {
      condition: (_unused, { getState }) => {
        return !getSlice(getState()).loading;
      },
    },
  );

  const apiSlice = createSlice({
    name: apiName,
    initialState,
    reducers: {},
    extraReducers: {
      [fetchThunk.pending.type]: state => {
        state.loading = true;
      },
      [fetchThunk.fulfilled.type]: (state, action) => {
        state.loading = false;
        state.entries = action.payload;
      },
      [fetchThunk.rejected.type]: state => {
        state.loading = false;
      },
    },
  });

  return {
    fetchThunk,
    reducer: apiSlice.reducer,
  };
}
