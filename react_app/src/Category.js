import React, { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'

export default function Category() {
  const [Dishes, fetchDishes] = useState([])
  const params = useParams();

  const getData = () => {
    fetch('http://127.0.0.1:8000/category/'+params.id)
      .then((res) => res.json())
      .then((res) => {
        fetchDishes(res)
      })
  }

  useEffect(() => {
    getData()
  }, [])

  return (
    <>
    <h3>Блюда выбранной категории</h3>
      {Dishes.map((item, i) => {
          return <><a href={'http://127.0.0.1:3000/dish/'+item.id}>{item.name}</a><br/></>
        })}
    </>
  )
}