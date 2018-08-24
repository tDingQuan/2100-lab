import Vue from 'vue'
import Router from 'vue-router'
import Homepage from '@/userviews/homepage/index'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/burnedcourse',
      name: 'BurnedCourse',
      component: () => import('@/userviews/burnedcoursepage/index')
    },
    {
      path: '/404',
      name: 'PageNotFound',
      component: () => import('@/userviews/pagenotfound/index')
    },
    {
      path: '/allfreecourse',
      name: 'AllFreeCourse',
      component: () => import('@/userviews/allcourselistpage/allFreeCoursePage')
    },
    {
      path: '/allpaidcourse',
      name: 'AllPaidCourse',
      component: () => import('@/userviews/allcourselistpage/allPaidCoursePage')
    },
    {
      path: '/personal',
      name: 'PersonalCenter',
      component: () => import('@/userviews/personal/personalCenter')
    },
    {
      path: '/studypage',
      name: 'StudyPage',
      component: () => import('@/userviews/studypage/index')
    },
    {
      path: '/',
      name: 'Homepage',
      component: Homepage
    },
    {
      path: '/login',
      name: 'Login',
      component: () => import('@/userviews/personal/login')
    },
    {
      path: '/personal/studylog',
      name: 'StudyLog',
      component: () => import('@/userviews/personal/log/studyLog')
    },
    {
      path: '/personal/orderlog',
      name: 'OrderLog',
      component: () => import('@/userviews/personal/log/orderLog')
    },
    {
      path: '/coursedetail',
      name: 'CourseDetail',
      component: () => import('@/userviews/coursedetail/index')
    },
    {
      path: '/admin',
      name: 'AdminLogin',
      component: () => import('@/adminviews/login')
    },
    {
      path: '/admin/main',
      name: 'Main',
      component: () => import('@/adminviews/main')
    },
    {
      path: '/admin/course',
      name: 'CourseManagement',
      component: () => import('@/adminviews/course/management')
    },
    {
      path: '/admin/course/detail',
      name: 'BackendCourseDetail',
      component: () => import('@/adminviews/course/detail')
    },
    {
      path: '/admin/course/creation',
      name: 'AddCourse',
      component: () => import('@/adminviews/course/add_course')
    },
    {
      path: '/admin/course/edit',
      name: 'EditCourse',
      component: () => import('@/adminviews/course/edit_course')
    },
    {
      path: '/admin/course/sync',
      name: 'SyncPicture',
      component: () => import('@/adminviews/course/synchronization')
    },
    {
      path: '/admin/message',
      name: 'MessageManagement',
      component: () => import('@/adminviews/message/management')
    },
    {
      path: '/admin/message/detail',
      name: 'MessageDetail',
      component: () => import('@/adminviews/message/detail')
    },
    {
      path: '/admin/adminmanagement',
      name: 'AdminManagement',
      component: () => import('@/adminviews/admin/management')
    },
    {
      path: '/admin/adminmanagement/changecode',
      name: 'ChangeCode',
      component: () => import('@/adminviews/admin/change_code')
    },
    {
      path: '/admin/adminmanagement/changename',
      name: 'ChangeName',
      component: () => import('@/adminviews/admin/change_name')
    },
    {
      path: '/admin/adminmanagement/distribution',
      name: 'DistributeAuthority',
      component: () => import('@/adminviews/admin/distribute_authority')
    },
    {
      path: '/admin/adminmanagement/detail',
      name: 'AdminDetail',
      component: () => import('@/adminviews/admin/detail')
    },
    {
      path: '/admin/adminmanagement/creation',
      name: 'AddAdmin',
      component: () => import('@/adminviews/admin/add_admin')
    },
    {
      path: '/admin/order',
      name: 'OrderManagement',
      component: () => import('@/adminviews/order/management')
    },
    {
      path: '/admin/order/detail',
      name: 'OrderDetail',
      component: () => import('@/adminviews/order/detail')
    },
    {
      path: '/admin/user',
      name: 'UserManagement',
      component: () => import('@/adminviews/user/management')
    },
    {
      path: '/admin/user/detail',
      name: 'UserDetail',
      component: () => import('@/adminviews/user/detail')
    },
    {
      path: '/admin/user/detail/course',
      name: 'Course',
      component: () => import('@/adminviews/user/course')
    },
    {
      path: '/admin/user/detail/order',
      name: 'Order',
      component: () => import('@/adminviews/user/order')
    },
    {
      path: '/admin/log',
      name: 'LogManagement',
      component: () => import('@/adminviews/log/management')
    },
    {
      path: '/admin/log/detail',
      name: 'LogDetail',
      component: () => import('@/adminviews/log/detail')
    },
    {
      path: '/admin/data',
      name: 'Data',
      component: () => import('@/adminviews/data/data')
    }
  ]
})
