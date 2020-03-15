import React from 'react'
import './board.css'
import _ from 'lodash'

function Board() {
  const size = 3
  const board = [['X', 'O', 'X'], ['O', 'O', ''], ['X', 'O', 'X'], []]
  const rows = _.times(size, (idx) => <Row key={idx} size={size} board={board[idx]} />)

  return (
    <div className="tictactoe-game">
      <div className="tictactoe-board">{rows}</div>
    </div>
  )
}

function Row(props) {
  const squares = _.times(props.size, (idx) => <Square key={idx} size={props.size} board={props.board[idx]} />)
  return <div className="tictactoe-row">{squares}</div>
}

function Square(props) {
  const fontStyle = {
    fontSize: 65 / props.size + 'vmin',
  }
  return (
    <div className="tictactoe-square">
      <span className="spacer" />
      <span style={fontStyle}>{props.board}</span>
      <span className="spacer" />
    </div>
  )
}

export default Board
