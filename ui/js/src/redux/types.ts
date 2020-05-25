export interface Episode {
  id: number;
  iteration: number;
  total_reward: number;
  training_run: number;
}

export interface Step {
  action: string | null;
  episode: number;
  id: number;
  info: string | null;
  is_done: boolean;
  iteration: number;
  reward: number;
  state: string;
}

export interface PlaybackEntry {
  moveInfo: {
    move: number[] | null;
    illegalMoves: number[][];
  };
  board: number[][] | null;
}

export interface TrainingRun {
  id: number;
}

export interface TrainingState {
  trainingRun: TrainingRun | null;
}

export interface PlaybackState {
  episode: number | null;
  logIdx: number | null;
  watchedEpisodes: number[];
}

export interface ApiState<T> {
  entries: T[];
  loading: boolean;
}

export interface ReduxState {
  episodesApi: ApiState<Episode>;
  stepsApi: ApiState<Step>;
  training: TrainingState;
  playback: PlaybackState;
}
