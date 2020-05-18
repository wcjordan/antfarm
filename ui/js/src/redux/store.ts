import { configureStore } from '@reduxjs/toolkit';
import rootReducer, { fetchEpisodes } from './reducers';

const store = configureStore({
  reducer: rootReducer,
});

// TODO dispose
window.setInterval(() => store.dispatch(fetchEpisodes()), 5 * 1000);
export default store;
