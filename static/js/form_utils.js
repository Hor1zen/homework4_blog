// form_utils.js - 表单相关的公共JavaScript工具函数

document.addEventListener('DOMContentLoaded', function() {
    const textArea = document.querySelector('textarea[name="text"]');
    const titleInput = document.querySelector('input[name="title"]');
    const textMaxLength = 10000;
    const titleMaxLength = 30;
    
    // 为内容文本框添加自动扩充、字数限制和显示
    if (textArea) {
        // 设置文本框样式
        textArea.style.resize = 'none';
        textArea.style.minHeight = '200px';
        
        // 创建字数显示元素
        const charCountElement = document.createElement('div');
        charCountElement.id = 'char-count';
        charCountElement.style.cssText = 'margin-top: 5px; font-size: 0.875em; color: #6c757d;';
        charCountElement.textContent = `字数: ${textArea.value.length}/${textMaxLength}`;
        
        // 将字数显示添加到文本框下方
        textArea.parentNode.appendChild(charCountElement);
        
        // 自动扩充函数
        function autoExpand() {
            textArea.style.height = 'auto';
            textArea.style.height = Math.max(textArea.scrollHeight, 200) + 'px';
        }
        
        // 添加输入事件监听器
        textArea.addEventListener('input', function() {
            // 限制字符数
            if (this.value.length > textMaxLength) {
                this.value = this.value.substring(0, textMaxLength);
            }
            
            // 自动扩充
            autoExpand();
            
            // 更新字数显示
            charCountElement.textContent = `字数: ${this.value.length}/${textMaxLength}`;
        });
        
        // 页面加载时也自动调整高度
        autoExpand();
    }
    
    // 为标题输入框添加字数限制和显示
    if (titleInput) {
        // 创建标题字数显示元素
        const titleCharCountElement = document.createElement('div');
        titleCharCountElement.id = 'title-char-count';
        titleCharCountElement.style.cssText = 'margin-top: 5px; font-size: 0.875em; color: #6c757d;';
        titleCharCountElement.textContent = `字数: ${titleInput.value.length}/${titleMaxLength}`;
        
        // 将字数显示添加到标题输入框下方
        titleInput.parentNode.appendChild(titleCharCountElement);
        
        // 添加输入事件监听器
        titleInput.addEventListener('input', function() {
            // 限制字符数
            if (this.value.length > titleMaxLength) {
                this.value = this.value.substring(0, titleMaxLength);
            }
            
            // 更新字数显示
            titleCharCountElement.textContent = `字数: ${this.value.length}/${titleMaxLength}`;
        });
    }
});