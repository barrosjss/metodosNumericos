import React from 'react'

export default function Secante() {
  return (
    <div className="col-lg-8 mx-auto p-4">
      <div className="Form">
        <form>
          <div className="mb-3">
            <label for="exampleFormControlInput1" class="form-label">Funcion</label>
            <input className="form-control" placeholder="Funcion por defecto: lambda x: x - math.cos(x)" disabled />
          </div>
          <div className="mb-3">
            <label for="exampleFormControlInput1" class="form-label">x0: Aproximación inicial de la solución.</label>
            <input className="form-control" placeholder="x0" />
          </div>
          <div className="mb-3">
            <label for="exampleFormControlInput1" class="form-label">x1: Otra aproximación inicial de la solución.</label>
            <input className="form-control" placeholder="x1" />
          </div>
          <div className="mb-3">
            <label for="exampleFormControlInput1" class="form-label">tol (tolerancia): Si abs(x1-x0)tol el algoritmo se detiene. </label>
            <input className="form-control" placeholder="tol" />
          </div>
          <button type="button" class="btn btn-dark">Dark</button>
        </form>
      </div>
    </div>
  )
}