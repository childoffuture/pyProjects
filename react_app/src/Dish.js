import React, { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'

export default function Dish() {
  const [Dish, fetchDish] = useState({})
  const params = useParams();

  const getData = () => {
    fetch('http://127.0.0.1:8000/dish/'+params.id)
      .then((res) => res.json())
      .then((res) => {
        fetchDish(res)
      })
  }

  useEffect(() => {
    getData()
  }, [])

  return (
    <>
      <h2>Рецепт блюда {Dish.name}</h2>
      <p>
        {Dish.description}
      </p>
    </>
  )
}