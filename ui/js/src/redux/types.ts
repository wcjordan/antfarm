export type Episode = {
  id: number;
  iteration: number;
  total_reward: number;
  training_run: number;
};

export type Step = {
  action: string | null;
  episode: number;
  id: number;
  info: string | null;
  is_done: boolean;
  iteration: number;
  reward: number;
  state: string;
};

export type TrainingRun = {
  id: number;
};
