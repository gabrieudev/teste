<template>
  <v-text-field
    :model-value="searchQuery"
    label="Digite sua pesquisa"
    variant="outlined"
    clearable
    @update:model-value="$emit('update:searchQuery', $event)"
    @keyup.enter="$emit('search')"
    :loading="loading"
  >
    <template v-slot:append>
      <v-btn color="primary" :disabled="!searchQuery" @click="$emit('search')" :loading="loading">
        <v-icon icon="mdi-magnify"></v-icon>
        <span class="ml-2">Buscar</span>
      </v-btn>
    </template>
  </v-text-field>
</template>

<script setup lang="ts">
defineProps({
  searchQuery: {
    type: String,
    required: true,
  },
  loading: {
    type: Boolean,
    default: false,
  },
})

defineEmits(['update:searchQuery', 'search'])
</script>
