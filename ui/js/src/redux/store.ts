import { configureStore } from '@reduxjs/toolkit';
import rootReducer, { fetchEpisodes, fetchSteps } from './reducers';
import { stepPlayback } from './reducers/playbackReducer';

const store = configureStore({
  reducer: rootReducer,
});

// TODO dispose
window.setInterval(() => store.dispatch(fetchEpisodes()), 1000);
window.setInterval(() => store.dispatch(fetchSteps()), 1000);
store.dispatch(stepPlayback());

export default store;
