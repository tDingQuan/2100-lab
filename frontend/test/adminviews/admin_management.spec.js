/* eslint-disable no-undef */

import { shallowMount } from '@vue/test-utils'
import AdminManagementBasic from '@/adminviews/admin/management.vue'

describe('管理员管理模块单元测验', () => {
  const wrapper = shallowMount(AdminManagementBasic)

  it('标题是"管理员列表"', () => {
    expect(wrapper.find('h2').text()).toEqual('管理员列表')
  })

  it('渲染查询输入框', () => {
    expect(wrapper.findAll('[type=text]').length).toEqual(2)
  })

  it('输入查询手机号内容正确显示', () => {
    wrapper.findAll('[type=text]').at(1).setValue('15222583257')
    expect(wrapper.vm.query_input[1]).toEqual('15222583257')
  })
})