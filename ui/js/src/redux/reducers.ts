import { Episode, Step } from './types';
import createApiReducer from './reducers/createApiReducer';
import playbackReducer from './reducers/playbackReducer';
import trainingReducer from './reducers/trainingReducer';

const {
  fetchThunk: fetchEpisodes,
  reducer: episodesReducer,
} = createApiReducer<Episode>(
  'episodesApi',
  'api/training/episodes/',
  state => state.episodesApi,
);

const { fetchThunk: fetchSteps, reducer: stepsReducer } = createApiReducer<
  Step
>('stepsApi', 'api/training/steps/', state => state.stepsApi);

export { fetchEpisodes, fetchSteps };
export default {
  episodesApi: episodesReducer,
  stepsApi: stepsReducer,
  training: trainingReducer,
  playback: playbackReducer,
};
