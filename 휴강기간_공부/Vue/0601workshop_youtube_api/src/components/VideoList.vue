<template>
  <div>
    <ul class="list-group">
    <VideoListitem class="py-1" @video-select="onVideoSelect" :video="video" v-for="video in videos" :key="video.etag"/>
    </ul>
  </div>
</template>

<script>
import VideoListitem from './VideoListitem.vue'
export default {
  name : 'VideoList',
  components : {
    VideoListitem
  },
  methods : {
    onVideoSelect(video){
      this.$emit('video-select',video)
    }
  },
  props : {
    videos : {
      type : Array
    }
  }
}
</script>

<style>

</style>