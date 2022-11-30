import React from 'react'
import Card from '../components/Card'

export default function Home() {
  return (
    <div className="col-lg-8 mx-auto p-4">
      <h1>🤓 Bienvenidos!</h1>
      <p class="fs-5 col-md-8 mb-5">La pagina esta dirigido a estudiantes de Ingeniería de Sistemas. El análisis numérico es una herramienta moderna que permite al estudiante resolver problemas de tipo profesional. Mediante el uso de modelos matemáticos complejos, el estudiante puede realizar cálculos muy elaborados.</p>
      <hr class="col-3 col-md-2 mb-5"></hr>

      <div class="row row-cols-1 row-cols-md-2 g-4">
        <Card
          title='Secante'
          description='Crear un código que permita la busqueda de la raiz de una ecuacion no lineal por medio del método de secante.'
          route='/secante'
        />
        <Card
          title='Lagranje'
          description='Código para taller de Interpolación de Lagrade con representación gráfica de puntos.'
          route='/lagranje'
        />
        <Card
          title='Biseccion'
          description='Crear un código que permita la busqueda de la raiz de una ecuacion no lineal por medio del método de bisección.'
          route=''
        />
        <Card
          title='Newton Raphson'
          description='Crear un código que permita la busqueda de la raiz de una ecuacion no lineal por medio del método de Newton Raphson.'
          route=''
        />
        <Card
          title='Newton Raphson'
          description='Crear un código que permita la busqueda de la raiz de una ecuacion no lineal por medio del método de Newton Raphson.'
          route=''
        />
      </div>
    </div>
  )
}
