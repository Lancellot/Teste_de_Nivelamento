<template>
    <div class="search-container">
      <h2>Buscar Operadora</h2>
  
      <div class="search-bar">
        <input 
          v-model="termo" 
          type="text" 
          placeholder="Digite o nome da operadora"
          :class="{'input-error': erro}"
          @keyup.enter="buscarOperadora"
        />
        <button @click="buscarOperadora" :disabled="loading">Buscar</button>
      </div>
  
      <div v-if="loading" class="loading">Carregando...</div>
  
      <div v-if="erro" class="error">{{ erro }}</div>
  
      <div v-if="resultados.length > 0" class="result-count">
        Total encontrado: {{ totalResultados }}
      </div>
  
      <div v-if="resultados.length > 0" class="resultados">
        <h3>Resultados:</h3>
        <ul>
          <li v-for="(item, index) in resultados" :key="index">
            <strong>{{ item.Nome_Fantasia || 'N/A' }}</strong> - 
            {{ item.Razao_Social || 'N/A' }} (CNPJ: {{ item.CNPJ || 'N/A' }})
            <div class="additional-info">
              <span v-if="item.Modalidade">Modalidade: {{ item.Modalidade }}</span>
              <span v-if="item.UF">UF: {{ item.UF }}</span>
            </div>
          </li>
        </ul>
      </div>
  
      <div v-if="termo && resultados.length === 0 && !erro" class="no-results">
        Nenhuma operadora encontrada. Tente novamente com outro termo.
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        termo: '',
        resultados: [],
        totalResultados: 0,
        erro: null,
        loading: false
      };
    },
    methods: {
      async buscarOperadora() {
        if (!this.termo.trim()) {
          this.erro = 'Por favor, digite um termo de busca.';
          return;
        }
  
        this.loading = true;
        this.erro = null;
        this.resultados = [];
        this.totalResultados = 0;
  
        try {
          const response = await fetch(
            `http://localhost:5000/buscar?termo=${encodeURIComponent(this.termo)}`,
            {
              headers: {
                'Accept': 'application/json',
              },
            }
          );
          
          if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.erro || 'Erro ao buscar operadora');
          }
  
          const data = await response.json();
          
          if (data.dados && data.dados.length > 0) {
            this.resultados = data.dados;
            this.totalResultados = data.total_resultados;
          } else {
            this.erro = 'Nenhuma operadora encontrada.';
          }
        } catch (error) {
          this.erro = error.message || 'Erro na requisição. Tente novamente.';
          console.error('Erro:', error);
        } finally {
          this.loading = false;
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .search-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    font-family: Arial, sans-serif;
  }
  
  .search-bar {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-bottom: 20px;
  }
  
  input {
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 4px;
    width: 70%;
    max-width: 400px;
  }
  
  button {
    padding: 10px 20px;
    background-color: #42b983;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  button:hover {
    background-color: #369f6b;
  }
  
  button:disabled {
    background-color: #cccccc;
    cursor: not-allowed;
  }
  
  .result-count {
    margin: 15px 0;
    font-weight: bold;
    color: #666;
  }
  
  .resultados ul {
    list-style: none;
    padding: 0;
    text-align: left;
  }
  
  .resultados li {
    padding: 15px;
    margin-bottom: 10px;
    background-color: #f8f9fa;
    border-radius: 4px;
    border-left: 4px solid #42b983;
  }
  
  .additional-info {
    margin-top: 8px;
    font-size: 14px;
    color: #666;
  }
  
  .additional-info span {
    display: inline-block;
    margin-right: 15px;
  }
  
  .loading, .error, .no-results {
    margin-top: 20px;
    padding: 10px;
    border-radius: 4px;
  }
  
  .loading {
    color: #666;
  }
  
  .error {
    color: #dc3545;
    background-color: #f8d7da;
    border: 1px solid #f5c6cb;
  }
  
  .no-results {
    color: #6c757d;
    background-color: #e2e3e5;
    border: 1px solid #d6d8db;
  }
  
  .input-error {
    border-color: #dc3545 !important;
  }
  </style>