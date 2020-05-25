import _ from 'lodash';
import React from 'react';
import { withKnobs, number } from '@storybook/addon-knobs';
import Board from './Board';

export default {
  title: 'Tictactoe Board',
  component: Board,
  decorators: [withKnobs],
};

const moveInfo = {
  move: null,
  illegalMoves: [],
};

export const DynamicBoard = () => (
  <Board
    size={number('Size', 3)}
    board={randomBoard(number('Size', 3))}
    moveInfo={moveInfo}
  />
);

export const Board3x3 = () => (
  <Board size={3} board={randomBoard(3)} moveInfo={moveInfo} />
);

export const Board4x4 = () => (
  <Board size={4} board={randomBoard(4)} moveInfo={moveInfo} />
);

export const Board5x5 = () => (
  <Board size={5} board={randomBoard(5)} moveInfo={moveInfo} />
);

export const Board7x7 = () => (
  <Board size={7} board={randomBoard(7)} moveInfo={moveInfo} />
);

export const Board10x10 = () => (
  <Board size={10} board={randomBoard(10)} moveInfo={moveInfo} />
);

const boardState = [
  [1, 1],
  [-1, 0],
];
const playerMoveInfo = {
  move: [0, 1],
  illegalMoves: [],
};
export const PlayerMove = () => (
  <Board size={2} board={boardState} moveInfo={playerMoveInfo} />
);

const opponentMoveInfo = {
  move: [1, 0],
  illegalMoves: [],
};
export const OpponentMove = () => (
  <Board size={2} board={boardState} moveInfo={opponentMoveInfo} />
);

const illegalMoveInfo = {
  move: [1, 0],
  illegalMoves: [
    [0, 1],
    [1, 0],
  ],
};
export const IllegalMove = () => (
  <Board size={2} board={boardState} moveInfo={illegalMoveInfo} />
);

const longMoveList = {
  move: null,
  illegalMoves: _.times(40, () => [0, 0]),
};
export const ScrollingVisor = () => (
  <Board size={2} board={null} moveInfo={longMoveList} />
);

function randomBoard(size: number) {
  return _.times(size, x => _.times(size, y => randomChar(x, y)));
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
