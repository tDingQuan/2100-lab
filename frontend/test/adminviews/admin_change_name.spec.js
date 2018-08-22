/* eslint-disable no-undef */

import { shallowMount } from '@vue/test-utils'
import ChangeName from '@/adminviews/admin/change_name.vue'

const $route = {
  path: '/admin/adminmanagement/changename',
  query: {'admin_id': 0}
}

describe('修改管理员名模块单元测验', () => {
  const wrapper = shallowMount(ChangeName, {
    mocks: {
      $route
    }
  })

  it('标题是"修改管理员名"', () => {
    expect(wrapper.find('h2').text()).toEqual('修改管理员名')
  })

  it('输入新管理员名', () => {
    expect(wrapper.vm.new_name).toEqual(null)
    wrapper.find('#newname').setValue('123456789')
    expect(wrapper.vm.new_name).toEqual('123456789')
  })
})