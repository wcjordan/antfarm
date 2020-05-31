import _ from 'lodash';
import React, { Component, SyntheticEvent } from 'react';
import { Episode } from '../../redux/types';
import './ControlPanel.css';

class ControlPanel extends Component<Props, State> {
  state = {
    disabled: false,
  };

  render() {
    const episodeControls = _.map(this.props.episodes, episode => {
      let entryClass = 'episode-entry';
      let iconClass = 'icon';
      if (episode.id === this.props.activeEpisode) {
        entryClass += ' active';
      } else if (this.props.watchedEpisodes.has(episode.id)) {
        entryClass += ' watched';
      }

      if (episode.id === this.props.activeEpisode) {
        if (this.props.paused) {
          iconClass += ' play paused';
        } else {
          iconClass += ' pause';
        }
      } else {
        iconClass += ' play';
      }

      return (
        <div key={episode.iteration} className={entryClass}>
          <div className="iteration">{`#${formatIteration(
            episode.iteration,
          )}`}</div>
          <div className="reward">{`reward: ${episode.total_reward.toFixed(
            2,
          )}`}</div>
          <div
            className={iconClass}
            onClick={() => this.togglePlayback(episode.id)}
          />
        </div>
      );
    });

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

  togglePlayback = (episodeId: number) => {
    this.props.togglePlayback(episodeId);
  };
}

function formatIteration(iteration: number) {
  return ('000' + iteration).slice(-3);
}

type Props = {
  activeEpisode: number | null;
  episodes: Episode[];
  paused: boolean;
  startTraining: Function;
  togglePlayback: Function;
  watchedEpisodes: Set<number>;
};
type State = {
  disabled: boolean;
};

export default ControlPanel;
