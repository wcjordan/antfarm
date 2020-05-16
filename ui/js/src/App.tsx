import React, { Component } from 'react'
import { Episode, Step, TrainingRun } from './components/training/DataStream'
import Layout from './Layout'

class App extends Component<Props, State> {
  constructor(props: Props) {
    super(props)

    this.state = {
      episodes: [],
      steps: [],
      training_run: null,
    }

    // TODO destroy on unmount
    window.setInterval(this.fetchData.bind(this), 5 * 1000)
  }

  render() {
    return <Layout startTraining={this.startTraining} {...this.state} />
  }

  fetchData = () => {
    fetch('api/training/episodes/', this.getRequestOpts('GET'))
      .then(res => res.json())
      .then(res => {
        this.setState({
          episodes: res,
        })
      })

    fetch('api/training/steps/', this.getRequestOpts('GET'))
      .then(res => res.json())
      .then(res => {
        this.setState({
          steps: res,
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
  episodes: Episode[]
  steps: Step[]
  training_run: TrainingRun | null
}

export default App
