<template>
  <div class="pagination-wrapper mt-4 d-flex align-center justify-space-between">
    <span class="text-caption">
      Mostrando {{ startItem }} - {{ endItem }} de {{ totalResults }}
    </span>

    <v-pagination
      :model-value="currentPage"
      :length="totalPages"
      @update:model-value="handlePageChange"
    />
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps({
  currentPage: {
    type: Number,
    required: true,
  },
  totalPages: {
    type: Number,
    required: true,
  },
  totalResults: {
    type: Number,
    required: true,
  },
  itemsPerPage: {
    type: Number,
    required: true,
  },
})

const emit = defineEmits(['update:current-page', 'page-changed'])

const startItem = computed(() => (props.currentPage - 1) * props.itemsPerPage + 1)
const endItem = computed(() => Math.min(props.currentPage * props.itemsPerPage, props.totalResults))

const handlePageChange = (newPage: number) => {
  emit('update:current-page', newPage)
  emit('page-changed')
}
</script>
