import React from 'react'
import Layout from './Layout'
import { action } from '@storybook/addon-actions'

export default {
  title: 'Layout',
  component: Layout,
}

export const DefaultLayout = () => (
  <Layout startTraining={action('start_training')} />
)
