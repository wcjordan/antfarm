import _ from 'lodash';
import { createSelector } from '@reduxjs/toolkit';
import { ReduxState } from './types';

const selectAllSteps = (state: ReduxState) => state.stepsApi.entries;
const selectAllEpisodes = (state: ReduxState) => state.episodesApi.entries;
const selectTrainingRunId = (state: ReduxState) =>
  state.training.trainingRun ? state.training.trainingRun.id : undefined;
const selectEpisodeIter = (state: ReduxState) => state.playback.episode;
const selectStepIter = (state: ReduxState) => state.playback.step;

export const selectEpisodes = createSelector(
  [selectAllEpisodes, selectTrainingRunId],
  (episodes, trainingRunId) =>
    _.sortBy(
      _.filter(episodes, episode => episode.training_run === trainingRunId),
      'iteration',
    ),
);

export const selectPlaybackEpisode = createSelector(
  [selectEpisodes, selectEpisodeIter],
  (episodes, iteration) => findEntry(episodes, iteration, 'episode'),
);

export const selectSteps = createSelector(
  [selectAllSteps, selectPlaybackEpisode],
  (steps, episode) => {
    const episodeId = episode ? episode.id : null;
    return _.sortBy(
      _.filter(steps, step => step.episode === episodeId),
      'iteration',
    );
  },
);

export const selectPlaybackStep = createSelector(
  [selectSteps, selectStepIter],
  (steps, iteration) => findEntry(steps, iteration, 'step'),
);

export const selectOpponentMove = createSelector(
  [selectSteps, selectPlaybackStep, selectStepIter],
  (steps, playbackStep, iteration) => {
    if (iteration === null || playbackStep === null) {
      return 'null';
    }

    const currBoard = JSON.parse(playbackStep.state);
    const previousStep = findEntry(steps, iteration - 1, 'step');
    let prevBoard = null;
    if (previousStep) {
      prevBoard = JSON.parse(previousStep.state);
    }

    for (let yIdx = 0; yIdx < currBoard.length; yIdx++) {
      for (let xIdx = 0; xIdx < currBoard[yIdx].length; xIdx++) {
        if (
          currBoard[yIdx][xIdx] === -1 &&
          (!prevBoard || prevBoard[yIdx][xIdx] !== -1)
        ) {
          return `[${yIdx}, ${xIdx}]`;
        }
      }
    }

    return 'null';
  },
);

interface Entry {
  iteration: number;
}
function findEntry<T extends Entry>(
  entries: T[],
  iteration: number | null,
  entryName: string,
) {
  const matches = _.filter(entries, entry => entry.iteration === iteration);
  if (matches.length > 1) {
    console.log(
      `WARNING found more than one ${entryName} in training run w/ iteration ${iteration}`,
    );
  }
  return _.first(matches) || null;
}
