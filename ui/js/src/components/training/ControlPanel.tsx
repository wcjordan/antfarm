import React, { Component, SyntheticEvent } from 'react'
import './ControlPanel.css'

class ControlPanel extends Component<Props, State> {
  static defaultProps = {
    disabled: false,
  }

  render() {
    return (
      <div className="control-panel">
        <div className="placeholder" />
        <div className="button start-button" onClick={this.startTraining}>
          Start Training
        </div>
      </div>
    )
  }

  startTraining = (event: SyntheticEvent<HTMLElement>) => {
    if (!this.props.disabled) {
      event.preventDefault()
      this.props.startTrainingHandler()
    }
  }
}

type Props = {
  disabled: boolean
  startTrainingHandler: Function
}

type State = {}

export default ControlPanel
