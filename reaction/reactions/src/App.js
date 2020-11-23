import logo from './logo.svg';
import './App.css';
import React from 'react';

class Panel extends React.Component {
  constructor(props) {
    super(props);
    this.state = { start_time: 0, ran_once: false, counting: false, true_duration: 0, reaction_time: 0, color: 'green'};
    this.process_click = this.process_click.bind(this);
  }
  handle_color = (c) => {
    // TODO: Your code here!
    this.setState({ color: c })

  }
  start_count() {
    // random float between 2000ms and 7000ms
    let time = 1000.0 * (1.0 + Math.random() * 6.0)
  
    this.setState({
      start_time: window.performance.now(),
      true_duration: time, 
      counting: true,
      color: 'darkred'
    });

    // change color to green after true_duration has elapsed
    setTimeout(() => this.handle_color("green"), time);
  }
  end_count() {
    // calculate elapsed time
    let elapsed = window.performance.now() - this.state.start_time;
    // do nothing if button should not be clicked yet
    if (elapsed > this.state.true_duration) {
      this.setState({
        ran_once: true,
        counting: false,
        reaction_time: elapsed - this.state.true_duration
      });
    }
  }
  process_click() {
    if (this.state.counting) {
      this.end_count();
    } else this.start_count();
  }
  render() {
    // handle msg
    let msg = ""
    if (this.state.counting) {
      if (this.state.color === 'darkred') {
        msg = "Wait for Green"
      } else if (this.state.color === 'green') {
        msg = "Click!"
      }
    } else {
      if (this.state.ran_once) {
        msg = "Your reaction time is " + Math.round(this.state.reaction_time).toString() + " ms"
      } else {
        msg = "Click me to begin!"
      }
    }

    return (
      <div className = "PanelContainer" onClick = {this.process_click} style={ { background: this.state.color} }>
        <div className = "Panel">{msg}</div>
      </div>
    );
  }
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1 className =  "Header">How Fast is your Reaction Time?</h1>
        <Panel />
        <p>Click as soon as the red box turns green. Click anywhere in the box to start.</p>
      </header>
    </div>
  );
}

export default App;
