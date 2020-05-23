import _ from 'lodash';
import React from 'react';
import { withKnobs, number } from '@storybook/addon-knobs';
import Board from './Board';

export default {
  title: 'Tictactoe Board',
  component: Board,
  decorators: [withKnobs],
};

export const DynamicBoard = () => (
  <Board size={number('Size', 3)} boardState={randomBoard(number('Size', 3))} />
);

export const Board3x3 = () => <Board size={3} boardState={randomBoard(3)} />;

export const Board4x4 = () => <Board size={4} boardState={randomBoard(4)} />;

export const Board5x5 = () => <Board size={5} boardState={randomBoard(5)} />;

export const Board7x7 = () => <Board size={7} boardState={randomBoard(7)} />;

export const Board10x10 = () => (
  <Board size={10} boardState={randomBoard(10)} />
);

const boardState = JSON.stringify([
  [1, 1],
  [-1, 0],
]);
const playerMoveInfo = {
  opponentMove: '[1, 0]',
  playerMove: '[0, 1]',
  playerMoveStep: true,
};
export const PlayerMove = () => (
  <Board size={2} boardState={boardState} moveInfo={playerMoveInfo} />
);

const opponentMoveInfo = Object.assign({}, playerMoveInfo, {
  playerMoveStep: false,
});
export const OpponentMove = () => (
  <Board size={2} boardState={boardState} moveInfo={opponentMoveInfo} />
);

function randomBoard(size: number) {
  return JSON.stringify(
    _.times(size, x => _.times(size, y => randomChar(x, y))),
  );
}

function randomChar(x: number, y: number) {
  const rand = Math.sin(3 * x + y);
  if (rand < 0.4) {
    return 1;
  }
  if (rand > 0.6) {
    return -1;
  }
  return 0;
}
