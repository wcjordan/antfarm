import Board from './components/tictactoe/Board'
import React, {Component} from 'react'
import './App.css'

interface Props {}

class App extends Component {
  constructor(props: Props) {
    super(props);

    this.state = {
      episodes: [],
    };
    this.fetchData();
  }

  render() {
    return (
      <div className="App">
        <Board size={3} />
      </div>
    )
  }

  fetchData() {
    const opts: RequestInit = {
      credentials: 'same-origin',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      method: 'GET',
    };
    fetch('api/train/episodes', opts)
      .then(res => res.json())
      .then(res => {
        this.setState({
          episodes: res,
        });
      });
  }
}

export default App
