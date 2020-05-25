import _ from 'lodash';
import React, { Component, SyntheticEvent } from 'react';
import { Episode } from '../../redux/types';
import './ControlPanel.css';

class ControlPanel extends Component<Props, State> {
  static defaultProps = {
    episodes: [],
  };
  state = {
    disabled: false,
  };

  render() {
    const episodeControls = _.map(
      _.sortBy(this.props.episodes, episode => -1 * episode.iteration),
      episode => {
        let entryClass = 'episode-entry';
        if (episode.id === this.props.activeEpisode) {
          entryClass += ' active';
        } else if (this.props.watchedEpisodes.has(episode.iteration)) {
          entryClass += ' watched';
        }
        return (
          <div className={entryClass}>
            <div className="iteration">{`#${formatIteration(
              episode.iteration,
            )}`}</div>
            <div className="reward">{`reward: ${episode.total_reward.toFixed(
              2,
            )}`}</div>
          </div>
        );
      },
    );

    let buttonClass = 'button';
    if (this.state.disabled) {
      buttonClass += ' disabled';
    }
    return (
      <div className="control-panel">
        <div className="episode-control">{episodeControls}</div>
        <div className={buttonClass} onClick={this.startTraining}>
          Start Training
        </div>
      </div>
    );
  }

  startTraining = (event: SyntheticEvent<HTMLElement>) => {
    if (!this.state.disabled) {
      this.setState({ disabled: true });
      event.preventDefault();
      this.props.startTraining();
    }
  };
}

function formatIteration(iteration: number) {
  return ('000' + iteration).slice(-3);
}

type Props = {
  activeEpisode: number | null;
  episodes: Episode[];
  startTraining: Function;
  watchedEpisodes: Set<number>;
};
type State = {
  disabled: boolean;
};

export default ControlPanel;
