import _ from 'lodash';
import React from 'react';
import './Board.css';

interface MoveProps {
  move: number[] | null;
  illegalMoves: number[][];
}
interface BoardProps {
  board: number[][] | null;
  moveInfo: MoveProps;
  size: number;
}
interface RowProps {
  board: number[];
  index: number;
  moveInfo: MoveProps;
  size: number;
}
interface SquareProps {
  activeMove: boolean;
  illegalMove: boolean;
  size: number;
  value: string;
}
interface WarningProps {
  message: string;
}

function Board(props: BoardProps) {
  const { size, moveInfo } = props;
  const board = getBoard(props.board);
  const rows = _.times(size, idx => (
    <Row
      key={idx}
      index={idx}
      size={size}
      board={board[idx]}
      moveInfo={moveInfo}
    />
  ));

  const warnings = _.map(moveInfo.illegalMoves, (move, key) => (
    <Warning
      key={key}
      message={`Space alread occupied - row: ${move[0]}, col: ${move[1]}.`}
    />
  ));

  return (
    <div className="tictactoe-game">
      <div className="tictactoe-board">{rows}</div>
      <div className="tictactoe-visor">
        <div className="visor-space" />
        <div className="tictactoe-warning-list">{warnings}</div>
      </div>
    </div>
  );
}

function Row(props: RowProps) {
  const { board, size, moveInfo, index: rowIdx } = props;
  const squares = _.times(size, colIdx => {
    let value = board[colIdx];
    const activeMove = !!(
      moveInfo.move &&
      moveInfo.move[0] === rowIdx &&
      moveInfo.move[1] === colIdx
    );
    const illegalMove = activeMove && moveInfo.illegalMoves.length > 0;
    return (
      <Square
        key={colIdx}
        size={size}
        value={renderChar(value)}
        activeMove={activeMove}
        illegalMove={illegalMove}
      />
    );
  });
  return <div className="tictactoe-row">{squares}</div>;
}

function Square(props: SquareProps) {
  const { activeMove, illegalMove } = props;
  const fontStyle = {
    fontSize: 65 / props.size + 'vmin',
  };
  const classes = illegalMove
    ? 'illegal-move'
    : activeMove
    ? 'active-move'
    : undefined;
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

function Warning(props: WarningProps) {
  return <div className="tictactoe-warning">{props.message}</div>;
}

function renderChar(value: number) {
  if (value === -1) {
    return 'O';
  } else if (value === 1) {
    return 'X';
  }
  return '';
}

function getBoard(boardOrNull: number[][] | null) {
  if (boardOrNull) {
    return boardOrNull;
  }
  return _.times(3, () => _.times(3, () => 0));
}

export default Board;
