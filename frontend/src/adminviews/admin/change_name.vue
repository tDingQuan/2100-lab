<template>
  <Basic :items="items">
    <div class="my-content">
      <h1>修改管理员名</h1>
      <Alert
        :count_down="wrong_count_down"
        :instruction="error_message"
        variant="danger"
        @decrease="wrong_count_down-1"
        @zero="wrong_count_down=0"/>
      <Alert
        :count_down="success_count_down"
        :instruction="error_message"
        variant="success"
        @decrease="success_count_down-1"
        @zero="success_count_down=0"/>
      <div>
        <div class="form-group">
          <h4
            class="form-check-label"
            for="newname">原管理员名：{{ old_name }}</h4>
        </div>
        <div class="form-group">
          <label
            class="form-check-label"
            for="newname">新管理员名</label>
          <input
            id="newname"
            v-model="new_name"
            class="input form-control col-lg-3"
            type="text">
        </div>
        <a
          id="save-btn"
          class="btn"
          @click="submit_message">
          保存
        </a>
      </div>
    </div>
  </Basic>
</template>

<script>
import Basic from '../basic/basic'
import axios from 'axios'
import qs from 'qs'
import Alert from '../../components/alert'
export default {
  name: 'ChangeName',
  components: { Alert, Basic },
  /**
   * @returns {{
   * items: *[], 路由跳转信息
   * new_name: null, 新用户名，不可为空
   * old_name: null, 旧用户名，从后端取得
   * wrong_count_down: number, 错误倒计时
   * success_count_down: number, 正确倒计时
   * error_message: string 错误信息提示
   * }}
   */
  data: function () {
    return {
      items: [
        {
          text: '主页',
          href: '/admin/main'
        },
        {
          text: '管理员管理',
          href: '/admin/adminmanagement'
        },
        {
          text: this.$route.query.admin_id.toString(),
          href:
            '/admin/adminmanagement/detail?admin_id=' +
            this.$route.query.admin_id.toString()
        },
        {
          text: '修改管理员名',
          active: true
        }
      ],
      new_name: null,
      old_name: null,
      wrong_count_down: 0,
      success_count_down: 0,
      error_message: ''
    }
  },
  /**
   * 向后端发送请求，发送用户ID
   * 得到回应，赋值旧用户名
   * 得到错误，输出借用转换函数得到的错误信息
   */
  created () {
    axios
      .get(
        'http://localhost/api/v1/admin/backstage/admin-management/get-admin-detail/',
        {
          params: {
            admin_id: this.$route.query.admin_id
          }
        }
      )
      .then(response => {
        this.old_name = response.data.username
      })
      .catch(error => {
        this.wrong_count_down = 0
        this.success_count_down = 0
        this.error_message = this.init_error_message(error.response.data.message)
        this.wrong_count_down = 5
      })
  },
  methods: {
    /**
     * 发送请求函数
     * 新名字不为空，且不应该与旧名字相同
     *
     * 发送请求，发送用户ID和新名字
     * 得到回复，输出之后新名字的信息
     * 得到错误，输出五秒借用转换函数得到的错误信息
     */
    submit_message: function () {
      if (this.new_name === null) {
        this.error_message = '请输入新名字'
        this.wrong_count_down = 5
      } else if (this.old_name === this.new_name) {
        this.error_message = '新旧名字一致'
        this.wrong_count_down = 5
      } else {
        axios
          .post(
            'http://localhost/api/v1/admin/backstage/admin-management/change-admin-username/',
            qs.stringify({
              admin_id: this.$route.query.admin_id,
              new_username: this.new_name
            })
          )
          .then(response => {
            this.wrong_count_down = 0
            this.success_count_down = 3
            this.error_message =
              '修改姓名成功，新用户名为：' + response.data.new_username
            this.router_push()
          })
          .catch(error => {
            this.wrong_count_down = 0
            this.success_count_down = 0
            this.error_message = this.init_error_message(error.response.data.message)
            this.wrong_count_down = 5
          })
      }
    },
    router_push () {
      this.$router.push({
        name: 'AdminDetail',
        query: { admin_id: this.$route.query.admin_id }
      })
    },
    init_error_message (message) {
      switch (message) {
        case 'Access denied.':
          return '用户无权限，拒绝访问'
        case 'Object not found.':
          return '查询的对象不存在'
        case 'This username is already taken.':
          return '该用户名已存在'
        case 'Invalid username.':
          return '无效的用户名'
        default:
          return '数据库查询出错'
      }
    }
  }
}
</script>

<style scoped>
.my-content {
  padding: 20px;
  margin: 70px 20px 20px;
  text-align: left;
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
}

h1 {
  margin: 25px 15px;
  color: #204269;
  text-align: left;
}

label {
  margin-bottom: 5px;
  font-size: 14px;
  font-weight: bold;
}

.form-group {
  margin-top: 60px;
  margin-left: 15px;
}

#save-btn {
  color: white;
}

.btn {
  margin-top: 40px;
  margin-right: 3px;
  margin-left: 15px;
  color: white;
  text-align: right;
  background-color: #4db14d;
  border: 1px solid #d3d9df;
}

.btn:hover,
.btn:active {
  background-color: #449c44;
}
</style>
