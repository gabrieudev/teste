<template>
  <v-card class="mb-4" elevation="2">
    <v-card-item>
      <v-card-title class="text-primary">
        {{ operadora.nome_fantasia || operadora.razao_social }}
      </v-card-title>
      <v-card-subtitle>
        {{ operadora.razao_social }}
      </v-card-subtitle>
    </v-card-item>

    <v-card-text>
      <v-chip variant="outlined" color="primary" class="mr-2 mb-2">
        {{ operadora.registro_ans }}
      </v-chip>
      <v-chip variant="outlined" color="secondary" class="mr-2 mb-2">
        {{ formatCNPJ(operadora.cnpj) }}
      </v-chip>
    </v-card-text>
  </v-card>
</template>

<script setup lang="ts">
import type { Operadora } from '@/types/operadoras'

defineProps({
  operadora: {
    type: Object as () => Operadora,
    required: true,
  },
})

const formatCNPJ = (cnpj: string) => {
  return cnpj.replace(/^(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})$/, '$1.$2.$3/$4-$5')
}
</script>
