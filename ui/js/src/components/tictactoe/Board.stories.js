import React from 'react'
import Board from './Board.js'
import { withKnobs, number } from '@storybook/addon-knobs'

export default {
  title: 'Tictactoe Board',
  component: Board,
  decorators: [withKnobs],
}

export const DynamicBoard = () => <Board size={number('Size', 3)} />

export const Board3x3 = () => <Board size={3} />

export const Board4x4 = () => <Board size={4} />

export const Board5x5 = () => <Board size={5} />

export const Board7x7 = () => <Board size={7} />

export const Board10x10 = () => <Board size={10} />
