<template>
  <v-container class="mt-8">
    <v-row justify="center">
      <v-col cols="12" md="10" lg="8">
        <v-card class="pa-4" elevation="4">
          <v-card-title class="text-h4 mb-4 text-center text-primary">
            Busca de Operadoras
          </v-card-title>

          <SearchBar
            v-model:searchQuery="searchQuery"
            :loading="isLoading"
            @search="() => performSearch(true)"
          />

          <v-alert v-if="errorMessage" type="error" variant="tonal" class="mt-4">
            {{ errorMessage }}
          </v-alert>

          <v-progress-linear
            v-if="isLoading"
            indeterminate
            color="primary"
            class="mt-4"
          ></v-progress-linear>

          <v-list v-if="results && results.length > 0" class="mt-4">
            <div class="text-h6 mb-2">Resultados ({{ totalResults }})</div>

            <OperadoraCard
              v-for="operadora in results"
              :key="operadora.registro_ans"
              :operadora="operadora"
            />

            <PaginationControls
              v-model:current-page="currentPage"
              :total-pages="totalPages"
              :total-results="totalResults"
              :items-per-page="itemsPerPage"
              @page-changed="performSearch"
            />
          </v-list>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import SearchBar from '@/components/search/SearchBar.vue'
import OperadoraCard from '@/components/search/OperadoraCard.vue'
import PaginationControls from '@/components/search/PaginationControls.vue'
import { useOperadorasSearch } from '@/composables/useOperadorasSearch'
import { watch } from 'vue'

const {
  searchQuery,
  results,
  isLoading,
  errorMessage,
  currentPage,
  itemsPerPage,
  totalPages,
  totalResults,
  performSearch,
} = useOperadorasSearch()

watch(currentPage, (newPage, oldPage) => {
  if (newPage !== oldPage) {
    performSearch()
  }
})
</script>
