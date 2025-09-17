import React, { useState } from 'react'

function App() {
  const [formData, setFormData] = useState({
    fecha: '',
    fuente: '',
    ubicacion: '',
    consumo: ''
  })

  const [errors, setErrors] = useState({})
  const [isSubmitting, setIsSubmitting] = useState(false)
  const [submitSuccess, setSubmitSuccess] = useState(false)

  const fuentes = ['electricidad', 'gas', 'solar', 'eolica']
  const ubicaciones = ['Planta Norte', 'Planta Sur', 'Oficina Central', 'Almacen']

  const handleInputChange = (e) => {
    const { name, value } = e.target
    setFormData(prev => ({
      ...prev,
      [name]: value
    }))

    if (errors[name]) {
      setErrors(prev => ({
        ...prev,
        [name]: ''
      }))
    }
  }

  const validateForm = () => {
    const newErrors = {}

    if (!formData.fecha) {
      newErrors.fecha = 'La fecha es requerida'
    } else {
      const fechaSeleccionada = new Date(formData.fecha)
      const fechaActual = new Date()
      if (fechaSeleccionada > fechaActual) {
        newErrors.fecha = 'La fecha no puede ser futura'
      }
    }

    if (!formData.fuente) {
      newErrors.fuente = 'La fuente energética es requerida'
    }

    if (!formData.ubicacion) {
      newErrors.ubicacion = 'La ubicación es requerida'
    }

    if (!formData.consumo) {
      newErrors.consumo = 'El consumo es requerido'
    } else {
      const consumoNum = parseFloat(formData.consumo)
      if (isNaN(consumoNum) || consumoNum <= 0) {
        newErrors.consumo = 'El consumo debe ser un número positivo'
      }
    }

    setErrors(newErrors)
    return Object.keys(newErrors).length === 0
  }

  const simulateApiCall = (data) => {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        console.log('Datos enviados al backend:', data)

        if (Math.random() > 0.1) {
          resolve({
            success: true,
            message: 'Consumo registrado exitosamente',
            id: Math.floor(Math.random() * 1000)
          })
        } else {
          reject(new Error('Error simulado del servidor'))
        }
      }, 1500)
    })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()

    if (!validateForm()) {
      return
    }

    setIsSubmitting(true)
    setSubmitSuccess(false)

    try {
      const result = await simulateApiCall({
        ...formData,
        consumo_kwh: parseFloat(formData.consumo),
        timestamp: new Date().toISOString()
      })

      console.log('Respuesta del servidor:', result)
      setSubmitSuccess(true)
      setFormData({
        fecha: '',
        fuente: '',
        ubicacion: '',
        consumo: ''
      })
    } catch (error) {
      console.error('Error al enviar datos:', error)
      setErrors({ submit: 'Error al conectar con el servidor. Intente nuevamente.' })
    } finally {
      setIsSubmitting(false)
    }
  }

  return (
    <div className="app">
      <div className="container">
        <div className="header">
          <h1>Energy Master <span className="energy-icon">⚡</span></h1>
          <p>Sistema de Registro de Consumos Energéticos</p>
        </div>

        <div className="form-container">
          {submitSuccess && (
            <div className="success-message">
              Consumo energético registrado exitosamente
            </div>
          )}

          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="fecha">📅 Fecha de Consumo:</label>
              <div className="input-wrapper">
                <input
                  type="date"
                  id="fecha"
                  name="fecha"
                  value={formData.fecha}
                  onChange={handleInputChange}
                  className={errors.fecha ? 'input-error' : ''}
                />
              </div>
              {errors.fecha && <div className="error">{errors.fecha}</div>}
            </div>

            <div className="form-group">
              <label htmlFor="fuente">⚡ Fuente Energética:</label>
              <div className="input-wrapper">
                <select
                  id="fuente"
                  name="fuente"
                  value={formData.fuente}
                  onChange={handleInputChange}
                  className={errors.fuente ? 'input-error' : ''}
                >
                  <option value="">Seleccione una fuente energética</option>
                  {fuentes.map(fuente => (
                    <option key={fuente} value={fuente}>
                      {fuente.charAt(0).toUpperCase() + fuente.slice(1)}
                    </option>
                  ))}
                </select>
              </div>
              {errors.fuente && <div className="error">{errors.fuente}</div>}
            </div>

            <div className="form-group">
              <label htmlFor="ubicacion">🏢 Ubicación:</label>
              <div className="input-wrapper">
                <select
                  id="ubicacion"
                  name="ubicacion"
                  value={formData.ubicacion}
                  onChange={handleInputChange}
                  className={errors.ubicacion ? 'input-error' : ''}
                >
                  <option value="">Seleccione una ubicación</option>
                  {ubicaciones.map(ubicacion => (
                    <option key={ubicacion} value={ubicacion}>
                      {ubicacion}
                    </option>
                  ))}
                </select>
              </div>
              {errors.ubicacion && <div className="error">{errors.ubicacion}</div>}
            </div>

            <div className="form-group">
              <label htmlFor="consumo">🔋 Consumo (kWh):</label>
              <div className="input-wrapper">
                <input
                  type="number"
                  id="consumo"
                  name="consumo"
                  value={formData.consumo}
                  onChange={handleInputChange}
                  placeholder="Ingrese el consumo en kWh (ej: 150.5)"
                  step="0.1"
                  className={errors.consumo ? 'input-error' : ''}
                />
              </div>
              {errors.consumo && <div className="error">{errors.consumo}</div>}
            </div>

            {errors.submit && <div className="error">{errors.submit}</div>}

            <button type="submit" disabled={isSubmitting} className="submit-button">
              {isSubmitting ? (
                <div className="loading-text">
                  <div className="loading-spinner"></div>
                  Procesando datos...
                </div>
              ) : (
                '🚀 Registrar Consumo Energético'
              )}
            </button>
          </form>
        </div>
      </div>
    </div>
  )
}

export default App