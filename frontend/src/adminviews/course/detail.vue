<template>
  <div>
    <div>
      <AdminNavbar/>
    </div>
    <div style="display: flex;">
      <div>
        <Menu/>
      </div>
      <div class="father container-fluid">
        <BreadCrumb :items="items"/>
        <div class="my-row">
          <h2 class="my-list">课程详情</h2>
          <div class="button_group">
            <button
              type="button"
              class="row btn btn-primary btn-sm"
              @click="edit_course"
            >修改课程</button>
            <button
              type="button"
              class="row btn btn-primary btn-sm"
              @click="delete_course"
            >删除课程</button>
          </div>
        </div>
        <table
          class="table table-striped table-hover"
          width="100%">
          <tbody>
            <tr>
              <td class="head-td">
                课程代码
              </td>
              <td class="content-td">
                {{ course.ID }}
              </td>
            </tr>
            <tr>
              <td class="head-td">
                课程名
              </td>
              <td class="content-td">
                {{ course.name }}
              </td>
            </tr>
            <tr>
              <td class="head-td">
                阅后即焚时间
              </td>
              <td class="content-td">
                {{ course.time }}
              </td>
            </tr>
            <tr>
              <td class="head-td">
                价格
              </td>
              <td class="content-td">
                {{ course.price }}
              </td>
            </tr>            <tr>
              <td class="head-td">
                分销金比例
              </td>
              <td class="content-td">
                {{ course.percent }}
              </td>
            </tr>
            <tr>
              <td class="head-td">
                添加时间
              </td>
              <td class="content-td">
                {{ course.add_time }}
              </td>
            </tr>
            <tr>
              <td class="head-td">
                修改时间
              </td>
              <td class="content-td">
                {{ course.change_time }}
              </td>
            </tr>
          </tbody>
        </table>
        <div class="my-intro">
          <h3 class="text-left">课程简介</h3>
          <p class="text-justify">{{ course.introduction }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import AdminNavbar from '../components/navbar'
import Menu from '../components/menu'
import BreadCrumb from '../../components/breadCrumb'
export default {
  name: 'BackendCourseDetail',
  components: {BreadCrumb, Menu, AdminNavbar},
  data: function () {
    return {
      items: [{
        text: '主页',
        href: '/admin'
      }, {
        text: '课程管理',
        href: '/admin/course'
      }, {
        text: '课程详情',
        active: true
      }],
      course: {
        'ID': '123456',
        'name': 'ascmk',
        'time': 'akscnk',
        'price': 'ascmk',
        'percent': 'aslcm',
        'add_time': 'aslcmklamlc',
        'change_time': 'ak njksdjvksnjk',
        'introduction': 'sncklsndkjvbweuiaciusDnmcksndkjcshndovi;jpaoerjvoigeahngvuihwroigrioahnvhios '
      }
    }
  }
}
</script>

<style scoped>
  .father {
    min-width: 500px;
    padding: 0;
  }

  .my-list {
    margin-left: 25px;
  }

  .my-row {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin-top: 20px;
    margin-bottom: 20px;
  }

  .head-td {
    width: 35%;
  }

  .content-td {
    width: 65%;
  }

  .button_group {
    display: flex;
  }

  .btn {
    margin-right: 25px;
  }

  .my-intro {
    margin-left: 25px;
  }
</style>