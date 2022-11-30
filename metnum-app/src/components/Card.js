import React from 'react'
import { Link } from 'react-router-dom'

export default function Card(props) {
  return (
    <div class="col">
      <div className="card text-bg-dark mb-3">
        <div className="card-header">{props.header}</div>
        <div className="card-body">
          <h5 class="card-title">{props.title}</h5>
          <p class="card-text">{props.description}</p>
          <Link to={props.route} class="btn btn-light">Go run</Link>
        </div>
      </div>
    </div>

  )
}