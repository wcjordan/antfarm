import React from 'react'
import './board.css'
import _ from 'lodash'

function Board(props) {
  const { size } = props
  const board = randomBoard(size)
  const rows = _.times(size, (idx) => <Row key={idx} size={size} board={board[idx]} />)

  return (
    <div className="tictactoe-game">
      <div className="tictactoe-board">{rows}</div>
    </div>
  )
}

function Row(props) {
  const { board, size } = props
  const squares = _.times(size, (idx) => <Square key={idx} size={size} board={board[idx]} />)
  return <div className="tictactoe-row">{squares}</div>
}

function Square(props) {
  const { board } = props
  const fontStyle = {
    fontSize: 65 / props.size + 'vmin',
  }
  return (
    <div className="tictactoe-square">
      <span className="spacer" />
      <span style={fontStyle}>{board}</span>
      <span className="spacer" />
    </div>
  )
}

function randomBoard(size) {
  return _.times(size, (x) => _.times(size, (y) => randomChar(x, y)))
}

function randomChar(x, y) {
  const rand = Math.sin(3 * x + y)
  if (rand < 0.4) {
    return 'X'
  }
  if (rand > 0.6) {
    return 'O'
  }
  return ''
}

export default Board
