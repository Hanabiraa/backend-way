import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

// class based component
// class Square extends React.Component {
//     render() {
//         return (
//             <button
//                 className="square"
//                 onClick={() => this.props.onClick()}
//             >
//                 {this.props.value}
//             </button>
//         );
//     }
// }

// function based component
function Square(props) {
    return (
        <button
            className="square"
            onClick={props.onClick}
        >
            {props.value}
        </button>
    );
}


class Board extends React.Component {
    // it’s conventional to use on[Event] names for props
    // which represent events and handle[Event] for the methods
    // which handle the events.

    // handleClick(i) {
    // create a copy of the squares array using the slice() method
    // instead of modifying the existing array.

    // immutability is important

    // Data Change without Mutation
    // var player = {score: 1, name: 'Jeff'};
    //
    // var newPlayer = Object.assign({}, player, {score: 2});
    // Now player is unchanged, but newPlayer is {score: 2, name: 'Jeff'}

    // Or if you are using object spread syntax, you can write:
    // var newPlayer = {...player, score: 2};

    // we gain several benefits described below with immutable objects.
    // 1) Complex Features Become Simple
    // 2) Detecting Changes
    // 3) Determining When to Re-Render in React

    //     const squares = this.state.squares.slice()
    //     if (calculateWinner(squares) || squares[i]) {
    //         return
    //     }
    //
    //     squares[i] = this.state.xIsNext ? 'X' : 'O'
    //     this.setState(
    //         {
    //             squares: squares,
    //             xIsNext: !this.state.xIsNext
    //         });
    // }

    renderSquare(i) {
        return <Square
            value={this.props.squares[i]}
            onClick={() => this.props.onClick(i)}
        />;
    }

    render() {
        return (
            <div>
                <div className="board-row">
                    {this.renderSquare(0)}
                    {this.renderSquare(1)}
                    {this.renderSquare(2)}
                </div>
                <div className="board-row">
                    {this.renderSquare(3)}
                    {this.renderSquare(4)}
                    {this.renderSquare(5)}
                </div>
                <div className="board-row">
                    {this.renderSquare(6)}
                    {this.renderSquare(7)}
                    {this.renderSquare(8)}
                </div>
            </div>
        );
    }
}

class Game extends React.Component {
    constructor(props) {
        // u need always call super(props) for react components class which have constructor
        super(props);
        this.state = {
            history: [
                {squares: Array(9).fill(null)}
            ],
            stepNumber: 0,
            xIsNext: true,
        }
    }

    handleClick(i) {
        const history = this.state.history.slice(0, this.state.stepNumber + 1);
        const current = history[history.length - 1];
        const squares = current.squares.slice();
        if (calculateWinner(squares) || squares[i]) {
            return;
        }
        squares[i] = this.state.xIsNext ? 'X' : 'O';
        // Unlike the array push() method you might be more familiar with,
        // the concat() method doesn’t mutate the original array, so we prefer it.
        this.setState({
            history: history.concat([{
                squares: squares,
            }]),
            stepNumber: history.length,
            xIsNext: !this.state.xIsNext,
        });
    }

    jumpTo(step) {
        // state updates are merged or in more simple words
        // React will update only the properties mentioned in setState method
        // leaving the remaining state as is.
        this.setState({
            stepNumber: step,
            xIsNext: (step % 2) === 0,
        });
    }

    render() {
        const history = this.state.history;
        const current = history[this.state.stepNumber];
        const winner = calculateWinner(current.squares);

        const moves = history.map((step, move) => {
            const desc = move ?
                'Go to move #' + move :
                'Go to game start';
            return (
                // It’s strongly recommended that you assign proper keys whenever
                // you build dynamic lists

                // If you don’t have an appropriate key, you may
                // want to consider restructuring your data so that you do.

                // React automatically uses key to decide which components to update.
                // A component cannot inquire about its key.
                <li key={move}>
                    <button onClick={() => this.jumpTo(move)}>{desc}</button>
                </li>
            );
        });

        let status;
        if (winner) {
            status = 'Winner: ' + winner;
        } else {
            status = 'Next player: ' + (this.state.xIsNext ? 'X' : 'O');
        }

        return (
            <div className="game">
                <div className="game-board">
                    <Board
                        squares={current.squares}
                        onClick={(i) => this.handleClick(i)}
                    />
                </div>
                <div className="game-info">
                    <div>{status}</div>
                    <ol>{moves}</ol>
                </div>
            </div>
        );
    }
}


// ========================================

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Game/>);

function calculateWinner(squares) {
    const lines = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ];
    for (let i = 0; i < lines.length; i++) {
        const [a, b, c] = lines[i];
        if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
            return squares[a];
        }
    }
    return null;
}
