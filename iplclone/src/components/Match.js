import React, {Component} from 'react';
import {Tabs, Tab} from 'react-bootstrap';


export default class Match extends Component {
    constructor(props) {
        super(props);

        this.state = {
            match_id: props.match.params.match_id,
            innings1: [],
            innings2: [],
            key: 'innings1',
            top_run_scorers: [],
            top_wicket_takers: [],
            extras_conceded: [],
            match_loaded: false,
            deliveries_loaded: false,
            error: false
        }
    }

    componentDidMount() {
        fetch('http://localhost:8000/api/v1/matches/' + String(this.state.match_id))
            .then(raw_data => raw_data.json().then(data => {
                console.log(data)
                this.setState({match: data, loaded: true})
            })).catch(err => {
                this.setState({error: true})
            })

        fetch('http://localhost:8000/api/v1/matches/'+String(this.state.match_id)+'/deliveries/innings/'+String(1))
        .then(raw_data => raw_data.json().then(data => {
                console.log(data)
                this.setState({innings1: data})
            })).catch(err => {
                this.setState({error: true})
            })

        fetch('http://localhost:8000/api/v1/matches/'+String(this.state.match_id)+'/deliveries/innings/'+String(2))
        .then(raw_data => raw_data.json().then(data => {
                console.log(data)
                this.setState({innings2: data})
            })).catch(err => {
                this.setState({error: true})
            })

        fetch('http://localhost:8000/api/v1/matches/'+String(this.state.match_id)+'/deliveries/top_run_scorer/')
        .then(raw_data => raw_data.json().then(data => {
                console.log(data)
                this.setState({top_run_scorer: data})
            })).catch(err => {
                this.setState({error: true})
            })

        fetch('http://localhost:8000/api/v1/matches/'+String(this.state.match_id)+'/deliveries/top_wicket_takers/')
        .then(raw_data => raw_data.json().then(data => {
                console.log(data)
                this.setState({top_wicket_takers: data})
            })).catch(err => {
                this.setState({error: true})
            })

         fetch('http://localhost:8000/api/v1/matches/'+String(this.state.match_id)+'/deliveries/extras_conceded/')
        .then(raw_data => raw_data.json().then(data => {
                console.log(data)
                this.setState({extras_conceded: data})
            })).catch(err => {
                this.setState({error: true})
            })
    }

    render() {
        if (this.state.loaded !== true) return <h1>Loading...</h1>

        return (
            <div class="container">
                <br/>
                <h2 align="center">{this.state.match.team1} vs {this.state.match.team2}</h2>
                <br/>
                <h4 align="center">Match details</h4>
                <MatchData match_data={this.state.match}/>
                <br/>
                <h4 align="center">Top Run Scorers</h4>
                <TopRunScorersData top_run_scorer={this.state.top_run_scorer}/>
                <br/>
                <h4 align="center">Top Wicket Takers</h4>
                <TopWicketTakersData top_wicket_takers={this.state.top_wicket_takers}/>
                <br/>
                <h4 align="center">Extras Conceded</h4>
                <ExtrasConcededData extras_conceded={this.state.extras_conceded}/>
                <br/>
                <Tabs
                    id="controlled-innings-tab"
                    activeKey={this.state.key}
                    onSelect={key => this.setState({ key })}>
                    <Tab eventKey="innings1" title="Innings 1">
                    <br/>
                    <h4 align="center">Innings 1</h4>
                    <MatchRenderer deliveries={this.state.innings1}/>
                    <br/>
                </Tab>
                <Tab eventKey="innings2" title="Innings 2">
                    <br/>
                    <h4 align="center">Innings 2</h4>
                    <MatchRenderer deliveries={this.state.innings2}/>
                    <br/>
                </Tab>
                </Tabs>
            <br/>
            </div>
        );
    }

}

const MatchData = props => {
    let data = props.match_data
    return (
        <div class="container">
        <br/>
            <table class="table table-hover">
                <tr><th>Date</th> <td>{data.date}</td></tr>
                <tr><th>Man of the Match</th> <td>{data.player_of_match}</td></tr>
                <tr><th>Toss Winner</th> <td>{data.toss_winner}</td></tr>
                <tr><th>Toss Decision</th> <td>{data.toss_decision}</td></tr>
                <tr><th>Venue</th> <td>{data.venue}</td></tr>
                <tr><th>Won by runs</th> <td>{data.win_by_runs}</td></tr>
                <tr><th>Won by wickets</th> <td>{data.win_by_wickets}</td></tr>
                <tr><th>Winner</th> <td>{data.winner}</td></tr>
            </table>
        <br/>
        </div>
    )
}

const TopRunScorersData = props => {
    return (
        <div class="container">
        <br/>
            <table class="table table-hover">
             <thead>
                    <tr>
                    <th>
                        Sl.No
                    </th>
                    <th>
                        Batsman
                    </th>
                    <th>
                        Team
                    </th>
                    <th>
                        Runs Scored
                    </th>
                    </tr>
                </thead>
            <tbody>
            {
           props.top_run_scorer.map((delivery, i) => {
                    return (
                        <tr>
                            <td>{i + 1}</td>
                            <td>{delivery.batsman}</td>
                            <td>{delivery.batting_team}</td>
                            <td>{delivery.batsman_runs}</td>
                        </tr>
                    )})
                }

            </tbody>
            </table>
        <br/>
        </div>
    )
}



const TopWicketTakersData = props => {
    let data = props.top_wicket_takers
    return (
        <div class="container">
        <br/>
            <table class="table table-hover">
             <thead>
                    <tr>
                    <th>
                        Sl.No
                    </th>
                    <th>
                        Bowler
                    </th>
                    <th>
                        Team
                    </th>
                    <th>
                        Wickets
                    </th>
                    </tr>
                </thead>
            <tbody>
            {
                data.map((record, i) => {
                    return (
                        <tr>
                            <td>{i + 1}</td>
                            <td>{record.bowler}</td>
                            <td>{record.bowling_team}</td>
                            <td>{record.total_runs}</td>
                        </tr>
                    )})
                }

            </tbody>
            </table>
        <br/>
        </div>
    )
}


const ExtrasConcededData = props => {
    return (
        <div class="container">
        <br/>
            <table class="table table-hover">
             <thead>
                    <tr>
                    <th>
                        Team
                    </th>
                    <th>
                        Extras
                    </th>
                    </tr>
             </thead>
            <tbody>
            {
           props.extras_conceded.map((delivery, i) => {
                    return (
                        <tr>
                            <td>{delivery.batting_team}</td>
                            <td>{delivery.total_runs}</td>
                        </tr>
                    )})
                }

            </tbody>
            </table>
        <br/>
        </div>
    )
}


const MatchRenderer = props => {
    return (
        <div class="container">
            <br/>
            <table class="table table-hover">
                <thead>
                    <tr><th>Over</th><th>Ball</th><th>Batsman</th><th>Non-striker</th><th>Bowler</th><th>Player dismissed</th><th>Dismissal kind</th><th>Total runs</th></tr>
                </thead>
                <tbody>
                    {
                        props.deliveries.map((data, i) => {
                            return (
                                <tr>
                                    <td>{data.over}</td>
                                    <td>{data.ball}</td>
                                    <td>{data.batsman}</td>
                                    <td>{data.non_striker}</td>
                                    <td>{data.bowler}</td>
                                    <td>{data.player_dismissed}</td>
                                    <td>{data.dismissal_kind}</td>
                                    <td>{data.total_runs}</td>
                                </tr>
                            )
                        })
                    }
                </tbody>
            </table>
            <br/>
        </div>
    )
}