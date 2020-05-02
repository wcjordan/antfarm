import React, { Component } from 'react'
import Layout from './Layout'

class App extends Component<Props, State> {
  constructor(props: Props) {
    super(props)

    this.state = {
      episodes: [],
      training_run: null,
    }
    this.fetchEpisodes()
  }

  render() {
    return <Layout startTraining={this.startTraining} />
  }

  fetchEpisodes = () => {
    fetch('api/training/episodes/', this.getRequestOpts('GET'))
      .then(res => res.json())
      .then(res => {
        this.setState({
          episodes: res,
        })
      })
  }

  startTraining = () => {
    const options = this.getRequestOpts('POST')
    options['body'] = JSON.stringify({
      name: 'test run ' + new Date().toLocaleString(),
    })

    fetch('api/training/training_runs/', options)
      .then(res => res.json())
      .then(res => {
        this.setState({
          training_run: res,
        })
      })
    console.log('Training started')
  }

  getRequestOpts(method: string): RequestInit {
    return {
      credentials: 'same-origin',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      method: method,
    }
  }
}

type Props = {}

type State = {
  episodes: object[]
  training_run: object | null
}

export default App
