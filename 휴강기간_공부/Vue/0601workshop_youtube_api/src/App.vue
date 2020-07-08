<template>
  <div class="container">
    <p>유튜브 클론코딩</p>
    <SearchBar @search-list="onSearchList"/>
    <div class='row'>
    <VideoDetail :videoDetail='videoDetail' class='col-7' />
    <VideoList :class="{'col-4': videoDetail, 'col-12':!videoDetail}"    @video-select="onVideoSelect" class='col-5' :videos="videos" />
    </div>
  </div>
</template>

<script>
import SearchBar from './components/SearchBar.vue'
import VideoList from './components/VideoList.vue'
import VideoDetail from './components/VideoDetail.vue'
import axios from 'axios'

const API_KEY = process.env.VUE_APP_API_KEY
const YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  data(){
    return {
      videos : [],
      videoDetail : null,
    }
  },
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
  },
  methods : {
    onSearchList(inputData){
      const params ={
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: inputData,

      }
      axios.get(YOUTUBE_URL,{params})
      .then((res) => {console.log(res)
          res.data.items.forEach(item =>{
            const parser = new DOMParser() // Parser을 해준다. 사용자가 쓸수있는데이터로 바꿔준다.
            const doc = parser.parseFromString(item.snippet.title,'text/html')
            console.log(doc)
            item.snippet.title = doc.body.innerText
          })
          this.videos = res.data.items
      })

    },
    onVideoSelect(video){
      this.videoDetail = video
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
