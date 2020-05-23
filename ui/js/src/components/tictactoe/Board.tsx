import _ from 'lodash';
import React from 'react';
import './Board.css';

interface MoveProps {
  opponentMove: string | null;
  playerMove: string | null;
  playerMoveStep: boolean;
}
interface BoardProps {
  size: number;
  boardState: string | null;
  moveInfo?: MoveProps;
}
interface RowProps {
  index: number;
  size: number;
  board: number[];
  moveInfo?: MoveProps;
}
interface SquareProps {
  size: number;
  value: string;
  activeMove: boolean;
}

function Board(props: BoardProps) {
  const { size, boardState, moveInfo } = props;

  let board = _.times(3, () => _.times(3, () => 0));
  if (boardState) {
    board = JSON.parse(boardState);
  }

  const rows = _.times(size, idx => (
    <Row
      key={idx}
      index={idx}
      size={size}
      board={board[idx]}
      moveInfo={moveInfo}
    />
  ));

  return (
    <div className="tictactoe-game">
      <div className="tictactoe-board">{rows}</div>
    </div>
  );
}

function Row(props: RowProps) {
  const { board, size, moveInfo, index: rowIdx } = props;
  const squares = _.times(size, colIdx => {
    let value = board[colIdx];
    let activeMove = false;
    const coord = `[${rowIdx}, ${colIdx}]`;
    if (moveInfo && coord === moveInfo.playerMove && moveInfo.playerMoveStep) {
      activeMove = true;
    }
    if (moveInfo && coord === moveInfo.opponentMove) {
      if (moveInfo.playerMoveStep) {
        value = 0;
      } else {
        activeMove = true;
      }
    }

    return (
      <Square
        key={colIdx}
        size={size}
        value={renderChar(value)}
        activeMove={activeMove}
      />
    );
  });
  return <div className="tictactoe-row">{squares}</div>;
}

function Square(props: SquareProps) {
  const fontStyle = {
    fontSize: 65 / props.size + 'vmin',
  };
  const classes = props.activeMove ? 'active-move' : undefined;
  return (
    <div className="tictactoe-square">
      <span className="spacer" />
      <span className={classes} style={fontStyle}>
        {props.value}
      </span>
      <span className="spacer" />
    </div>
  );
}

function renderChar(value: number) {
  if (value === -1) {
    return 'O';
  } else if (value === 1) {
    return 'X';
  }
  return '';
}

export default Board;
