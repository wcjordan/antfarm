import _ from 'lodash';
import { createSelector } from '@reduxjs/toolkit';
import { PlaybackEntry, ReduxState, SortMode } from './types';

const selectAllSteps = (state: ReduxState) => state.stepsApi.entries;
const selectAllEpisodes = (state: ReduxState) => state.episodesApi.entries;
const selectTrainingRunId = (state: ReduxState) =>
  state.training.trainingRun ? state.training.trainingRun.id : undefined;
const selectEpisodeId = (state: ReduxState) => state.playback.episodeId;
const selectPlaybackLogIdx = (state: ReduxState) => state.playback.logIdx;
const selectWatchedEpisodes = (state: ReduxState) =>
  state.playback.watchedEpisodes;
const selectSortMode = (state: ReduxState) => state.playback.sortMode;

export const selectWatchedSet = createSelector(
  [selectWatchedEpisodes],
  watchedEpisodes => new Set(watchedEpisodes),
);

export const selectDoneEpisodeSet = createSelector(
  [selectAllSteps],
  steps =>
    new Set(
      _.map(
        _.filter(steps, step => step.is_done),
        step => step.episode,
      ),
    ),
);

const selectEpisodesList = createSelector(
  [selectAllEpisodes, selectDoneEpisodeSet, selectTrainingRunId],
  (episodes, completeEpisodes, trainingRunId) =>
    _.filter(
      episodes,
      episode =>
        episode.training_run === trainingRunId &&
        completeEpisodes.has(episode.id),
    ),
);

const selectEpisodeMapById = createSelector([selectEpisodesList], episodes =>
  _.keyBy(episodes, episode => episode.id),
);

export const selectSortedEpisodes = createSelector(
  [selectEpisodesList, selectSortMode],
  (episodes, sortMode) =>
    _.sortBy(episodes, episode => {
      if (sortMode === SortMode.Iteration) {
        return -1 * episode.iteration;
      }
      return -1 * episode.total_reward;
    }),
);

export const selectPlaybackEpisode = createSelector(
  [selectEpisodeMapById, selectEpisodeId],
  (episodeMap, episodeId) =>
    episodeId !== null ? episodeMap[episodeId] : null,
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

export const selectPlaybackLog = createSelector([selectSteps], steps => {
  return _.reduce(
    steps,
    (result: PlaybackEntry[], step) => {
      const playerMove = step.action ? JSON.parse(step.action) : null;
      const currBoard = JSON.parse(step.state);

      const prevLogEntry = _.last(result);
      const prevBoard = prevLogEntry ? prevLogEntry.board : null;
      const opponentMove = getOpponentMove(currBoard, prevBoard);

      if (!playerMove) {
        result.push({
          board: currBoard,
          isDone: step.is_done,
          iteration: step.iteration,
          moveInfo: {
            move: null,
            illegalMoves: [],
          },
          reward: step.reward,
        });
        return result;
      }

      if (opponentMove) {
        const midStepBoard = _.cloneDeep(currBoard);
        midStepBoard[opponentMove[0]][opponentMove[1]] = 0;
        result.push({
          board: midStepBoard,
          isDone: false,
          iteration: step.iteration,
          moveInfo: {
            move: playerMove,
            illegalMoves: [],
          },
          reward: step.reward,
        });
        result.push({
          board: currBoard,
          isDone: step.is_done,
          iteration: step.iteration,
          moveInfo: {
            move: opponentMove,
            illegalMoves: [],
          },
          reward: step.reward,
        });
        return result;
      }

      const illegalMoves = step.is_done
        ? []
        : prevLogEntry
        ? [...prevLogEntry.moveInfo.illegalMoves, playerMove]
        : [playerMove];
      result.push({
        board: currBoard,
        isDone: step.is_done,
        iteration: step.iteration,
        moveInfo: {
          move: playerMove,
          illegalMoves,
        },
        reward: step.reward,
      });
      return result;
    },
    [],
  );
});

export const selectPlaybackEntry = createSelector(
  [selectPlaybackLog, selectPlaybackLogIdx],
  (log, logIdx) =>
    logIdx !== null && logIdx < log.length
      ? log[logIdx]
      : {
          board: null,
          isDone: false,
          iteration: 0,
          moveInfo: {
            move: null,
            illegalMoves: [],
          },
          reward: 0,
        },
);

function getOpponentMove(currBoard: number[][], prevBoard: number[][] | null) {
  for (let yIdx = 0; yIdx < currBoard.length; yIdx++) {
    for (let xIdx = 0; xIdx < currBoard[yIdx].length; xIdx++) {
      if (
        currBoard[yIdx][xIdx] === -1 &&
        (!prevBoard || prevBoard[yIdx][xIdx] !== -1)
      ) {
        return [yIdx, xIdx];
      }
    }
  }
  return null;
}
