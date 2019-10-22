import React, {Component} from 'react';
import ReactTable from "react-table";

export default class Season extends Component {
    constructor(props) {
        super(props);

        this.state = {
            seasons: [],
            matches: [],
            season: 2019,
            loaded: false,
            season_loaded: false,
            error: false
        }

        this.fetchSeason = this.fetchSeason.bind(this);
    }

    componentDidMount() {
        fetch('http://localhost:8000/api/v1/matches/seasons/')
            .then(raw_data => raw_data.json()
            .then(data => {
                this.setState({seasons: data, loaded: true})
            })).catch(err => {
                this.setState({error: true})
            })
        
        fetch('http://localhost:8000/api/v1/matches/seasons/2019/')
            .then(raw_data => raw_data.json().then(data => {
                this.setState({matches: data, matches_loaded: true})
            })).catch(err => {
                this.setState({error: true})
            })
    }


    fetchSeason(event) {
        var i = event.target.value
        this.setState({season_loaded: false});
        fetch('http://localhost:8000/api/v1/matches/seasons/' + String(i))
            .then(raw_data => raw_data.json().then(data => {
                this.setState({matches: data, season: i, season_loaded: true})
            })).catch(err => {
                this.setState({error: true})
            })
    }

    render() {
        if (this.state.loaded !== true) return <h1>Loading...</h1>
        return (
            <div>
                <DropDown seasons={this.state.seasons} onChange={this.fetchSeason}/>
                {
                    this.state.season_loaded === true  || this.state.loaded === true ?
                    <MatchesRenderer matches={this.state.matches} season={this.state.season}/>:
                    <h1>Loading...</h1>
                }
            </div>
        );
    }

}

const DropDown = props => {
    console.log(props)
    return (
    <div class="container">
        <br/>
        <select class="form-control" id="seasons-dropdown" onChange={props.onChange}>
            {
                 props.seasons.map(function (season) {
                 return <option key={season.season} value={season.season}>{season.season}</option>
            })
            }
        </select>
        <br/>
    </div>
    )
}

const MatchesRenderer = props => {
    console.log(props);
    return(
    <div class="container">
    <br/>
         <h3 align="center">List of matches in {props.season}</h3>
            <table class="table table-hover">
                <thead>
                    <tr>
                    <th>
                        Sl.No
                    </th>
                    <th>
                        Team1
                    </th>
                    <th>
                        Team2
                    </th>
                    <th>
                        Winner
                    </th>
                    <th>
                        Man of the Match
                    </th>
                    <th>
                        Date
                    </th>
                    <th>
                        Venue
                    </th>
                    <th>
                        More Info
                    </th>
                    </tr>
                </thead>
            <tbody>
            {
                props.matches.map((match, i) => {
                    return (
                        <tr>
                            <td>{i + 1}</td>
                            <td>{match.team1}</td>
                            <td>{match.team2}</td>
                            <td>{match.winner}</td>
                            <td>{match.player_of_match}</td>
                            <td>{match.date}</td>
                            <td>{match.venue}</td>
                            <td><button class="btn btn-info" onClick={() => window.location.href='http://localhost:3000/matches/' + String(match.match_id)}>Match Deatils</button></td>
                        </tr>
                    )})
                }

            </tbody>
            </table>
            <br/>
        </div>
    )
}