import { ref, computed } from 'vue'
import axios from 'axios'
import type { Operadora } from '@/types/operadoras'

export const useOperadorasSearch = () => {
  const searchQuery = ref('')
  const results = ref<Operadora[]>([])
  const isLoading = ref(false)
  const errorMessage = ref('')
  const currentPage = ref(1)
  const itemsPerPage = ref(10)
  const totalResults = ref(0)

  const totalPages = computed(() => {
    return Math.ceil(totalResults.value / itemsPerPage.value)
  })

  const performSearch = async (newSearch: boolean = false) => {
    if (newSearch) currentPage.value = 1

    if (!searchQuery.value?.trim()) {
      errorMessage.value = 'Por favor, digite um termo de pesquisa'
      results.value = []
      return
    }

    try {
      isLoading.value = true
      errorMessage.value = ''
      results.value = []

      const response = await axios.get(`${import.meta.env.VITE_API_BASE_URL}/search`, {
        params: {
          query: searchQuery.value.trim(),
          page: currentPage.value,
          size: itemsPerPage.value,
        },
      })

      if (response.status === 200) {
        if (response.data && Array.isArray(response.data.results)) {
          results.value = response.data.results
          totalResults.value = response.data.total
        } else {
          throw new Error('Formato de resposta inválido')
        }

        if (results.value.length === 0) {
          errorMessage.value = 'Nenhum resultado encontrado'
        }
      }
    } catch (error) {
      results.value = []
      if (axios.isAxiosError(error)) {
        errorMessage.value = error.response?.data?.error || 'Erro na busca'
      } else {
        errorMessage.value = error instanceof Error ? error.message : 'Erro desconhecido'
      }
    } finally {
      isLoading.value = false
    }
  }

  return {
    searchQuery,
    results,
    isLoading,
    errorMessage,
    currentPage,
    itemsPerPage,
    totalPages,
    totalResults,
    performSearch,
  }
}
