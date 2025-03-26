<script setup>
import { useMirrorList } from "../lib/mirrorList";
import { computed } from "vue";

const rawMirrorList = useMirrorList();

const nowBrowsingMirror = computed(() => {
  let mirrorName = location.pathname.split("/")[1]?.toLowerCase();
  if (!mirrorName) {
    return null;
  }
  const result = rawMirrorList.value.filter((m) => {
    return m.name.toLowerCase() === mirrorName;
  })[0];
  if (!result) {
    return null;
  }
  return result;
});
</script>

<template>
  <template v-if="nowBrowsingMirror">
    <strong>上次更新:&nbsp;</strong>
    <UpdateField :mir="nowBrowsingMirror"></UpdateField>
  </template>
</template>
