import _ from 'lodash'
import React from 'react'
import './DataStream.css'

const DataStream: React.SFC<Props> = props => {
  if (props.trainingRun === null) {
    return <div></div>
  }

  const trainingRunId = props.trainingRun.id
  const episodeElements = _.map(
    _.filter(props.episodes, episode => episode.training_run === trainingRunId),
    episode => renderEpisode(props.steps, episode),
  )

  return <div className="data-stream">{episodeElements}</div>
}

const renderEpisode = (steps: Step[], episode: Episode) => {
  const stepElements = _.map(
    _.filter(steps, step => step.episode === episode.id),
    step => renderStep(step),
  )

  return (
    <div key={episode.id}>
      {`#${episode.iteration} total reward ${episode.total_reward.toPrecision(
        2,
      )}`}
      {stepElements}
    </div>
  )
}

const renderStep = (step: Step) => {
  let completeElement = null
  if (step.is_done) {
    completeElement = <div>GAME OVER</div>
  }
  return (
    <div key={step.id} className="step">
      <div>{`  #${step.iteration} ${step.action} Reward: ${step.reward}`}</div>
      <div>{`    Info: ${step.info}`}</div>
      <div>{`    State: ${step.state}`}</div>
      {completeElement}
    </div>
  )
}

export type Episode = {
  id: number
  iteration: number
  total_reward: number
  training_run: number
}

export type Step = {
  action: string | null
  episode: number
  id: number
  info: string | null
  is_done: boolean
  iteration: number
  reward: number
  state: string
}

export type TrainingRun = {
  id: number
}

type Props = {
  episodes: Episode[]
  steps: Step[]
  trainingRun: TrainingRun | null
}

export default DataStream
